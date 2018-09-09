from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from courses.models import Course
from courses.serializers import CourseSerializer, IndexNavResponseSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCourseListView(APIView):
    def get_objects(self, pk):
        try:
            return Course.objects.filter(pk=pk)
        except Course.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        courses = self.get_objects(pk)
        serializer = IndexNavResponseSerializer(courses, many=True)
        return Response(serializer.data)
