from rest_framework import serializers
from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            'vid',
            'company',
            'address',
            'city',
            'province',
            'region',
            'linkman',
            'logo',
        ]


class VendorEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('company', 'address', 'city', 'province', 'country', 'region','linkman', 'cellphone')
