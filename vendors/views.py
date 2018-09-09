from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from rest_framework import generics
from .serializers import VendorSerializer
from .models import Vendor
from .forms import VendorCreateForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from  .serializers import VendorEditSerializer
from courses.models import Course
from categories.models import Category
from courses.serializers import CourseTableShowSerializer
import json




class VendorListView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


@receiver(post_save, sender=User)
def post_save_user_signal_handler(sender, instance, created, **kwargs):
    if created:
       instance.is_staff = True
       group = Group.objects.get(name='Vendors')
       instance.groups.add(group)
       instance.save()


def create_vendor_form(request):
    if request.method == "POST":
        form = VendorCreateForm(request.POST)
        if form.is_valid():
            form_item = form.save(commit=False)
            form_item.save()
    else:
        form = VendorCreateForm()
    return render(request, 'submit.html', {'form': form})


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密 码', widget=forms.PasswordInput())

@csrf_exempt
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)  # 包含用户名和密码
        if uf.is_valid():
            username = uf.cleaned_data['username']  # cleaned_data类型是字典，里面是提交成功后的信息
            password = uf.cleaned_data['password']
            try:
                User.objects.create_user(username=username, password=password)
                re = auth.authenticate(username=username, password=password)  # 用户认证
                if re is not None:  # 如果数据库里有记录（即与数据库里的数据相匹配或者对应或者符合）
                    auth.login(request, re)  # 登陆成功
                    return redirect('/home/')  # 跳转--redirect指从一个旧的url转到一个新的url
            except:
                return redirect('/register/')

    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        uf = UserForm()

    return render(request, 'register.html', {'uf': uf})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re = auth.authenticate(username=username, password=password)  #用户认证
        if re is not None:  #如果数据库里有记录（即与数据库里的数据相匹配或者对应或者符合）
            auth.login(request,re)   #登陆成功
            return redirect('/home/')    #跳转--redirect指从一个旧的url转到一个新的url
        else:  #数据库里不存在与之对应的数据
            return render(request, 'login.html', {'login_error':'用户名或密码错误'})  #注册失败
    return render(request, 'login.html')


@login_required
def home(request):
    try:
        vendor = Vendor.objects.get(authUser=request.user)
    except:
        vendor = Vendor(authUser=request.user, company=request.user.username)
        vendor.save()
    isAuth = vendor.isCertificated
    if isAuth == 0:
        return render(request, 'home.html', {'name':request.user.username, 'isAuth':isAuth})
    if isAuth == 1:
        company = vendor.company
        linkman = vendor.linkman
        return render(request, 'wait.html', {'name':request.user.username, 'company': company, 'linkman':linkman})
    else:
        course_list = Course.objects.filter(vendor=vendor)
        if course_list:
            company = vendor.company
            serializer = CourseTableShowSerializer(course_list, many=True)
            return render(request, 'manage.html', {'name':request.user.username, 'course_list':json.dumps(serializer.data), 'company': company})
        else:
            company = vendor.company
            list = []
            return render(request, 'manage.html', {'name': request.user.username, 'course_list': list, 'company': company})

def logout(request):
    auth.logout(request)
    return redirect('/login /')


class UploadLogoView(APIView):
    @csrf_exempt
    def post(self, request):
        image = request.data['image']
        user = User.objects.get(username=request.data['username'])
        vendor = Vendor.objects.get(authUser=user)
        vendor.logo = image
        vendor.save()
        return Response(status=status.HTTP_201_CREATED)


class UploadBLView(APIView):
    @csrf_exempt
    def post(self, request):
        image = request.data['image']
        user = User.objects.get(username=request.data['username'])
        vendor = Vendor.objects.get(authUser=user)
        vendor.business_license = image
        vendor.save()
        return Response(status=status.HTTP_201_CREATED)


class UploadEPView(APIView):
    @csrf_exempt
    def post(self, request):
        image = request.data['image']
        user = User.objects.get(username=request.data['username'])
        vendor = Vendor.objects.get(authUser=user)
        vendor.education_permit = image
        vendor.save()
        return Response(status=status.HTTP_201_CREATED)


class UploadRCView(APIView):
    @csrf_exempt
    def post(self, request):
        image = request.data['image']
        user = User.objects.get(username=request.data['username'])
        vendor = Vendor.objects.get(authUser=user)
        vendor.rental_contract = image
        vendor.save()
        return Response(status=status.HTTP_201_CREATED)


class UploadCourseView(APIView):
    @csrf_exempt
    def post(self, request):
        image = request.data['image']
        print(request.data)
        course = Course.objects.get(code=request.data['code'])
        course.showcase = image
        course.save()
        return Response(status=status.HTTP_201_CREATED)


class EditInfoView(APIView):
    @csrf_exempt
    def post(self, request):
        user = User.objects.get(username=request.data['username'])
        try:
            vendor = Vendor.objects.get(authUser=user)
            vendor.company = request.data['company']
            vendor.province = request.data['province']
            vendor.city = request.data['city']
            vendor.address = request.data['address']
            vendor.country = "中国"
            vendor.region = request.data['region']
            vendor.linkman = request.data['linkman']
            vendor.cellphone = request.data['cellphone']
            vendor.isCertificated = 1
            vendor.save()
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)


class AddCourseView(APIView):
    @csrf_exempt
    def post(self, request):
        user = User.objects.get(username=request.data['username'])
        vendor = Vendor.objects.get(authUser=user)
        tags = request.data['tag']
        tag_len = len(tags)
        print(tag_len)
        if tag_len == 0:
            tag1=""
            tag2=""
            tag3=""
        elif tag_len == 1:
            tag1=tags[0]
            tag2=""
            tag3=""
        elif tag_len == 2:
            tag1=tags[0]
            tag2=tags[1]
            tag3=""
        else:
            tag1=tags[0]
            tag2=tags[1]
            tag3=tags[2]

        cat = Category.objects.get(name=request.data['category'])
        course = Course(
            code=request.data['code'],
            name=request.data['name'],
            price=request.data['price'],
            club_price=request.data['club_price'],
            price_note=request.data['price_note'],
            description=request.data['description'],
            detail=request.data['detail'],
            vendor=vendor,
            categoryID=cat,
            tag1=tag1,
            tag2=tag2,
            tag3=tag3,
        )

        course.save()
        return Response(status=status.HTTP_201_CREATED)
