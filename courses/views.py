from rest_framework import generics
from .serializers import CourseSerializer, CourseDetailShowSerializer
from rest_framework.views import APIView
from .models import Course
from rest_framework.response import Response
from rest_framework import status



class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailShowView(APIView):
    def post(self, request):
        course = Course.objects.get(code=request.data['code'])
        serializer = CourseDetailShowSerializer(course)

        return Response(serializer.data, status=status.HTTP_200_OK)
