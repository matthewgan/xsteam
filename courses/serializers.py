from rest_framework import serializers
from .models import Course
from vendors.models import Vendor


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class IndexNavResponseSerializer(serializers.ModelSerializer):
    region = serializers.CharField(source='vendor.region')


    class Meta:
        model = Course
        fields = ('name', 'showcase', 'price', 'tag1', 'tag2', 'tag3', 'like', 'region', 'showcase', 'code', 'price_note')

class CourseDetailShowSerializer(serializers.ModelSerializer):
    vendor_logo = serializers.CharField(source='vendor.logo')
    vendor_name = serializers.CharField(source='vendor.company')
    vendor_location = serializers.CharField(source='vendor.address')
    vendor_tel = serializers.CharField(source='vendor.cellphone')

    class Meta:
        model = Course
        fields = ('code', 'name', 'showcase', 'price', 'vendor_logo', 'vendor_name', 'vendor_location', 'vendor_tel', 'service', 'review_point'
                  , 'review_number', 'description', 'detail')


class CourseTableShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'code', 'price',)