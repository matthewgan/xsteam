import uuid
from django.db import models


def upload_logo_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s.%s" % (instance.vid, "logo", extension)


def upload_permit_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s.%s" % (instance.vid, "cert", extension)


def upload_license_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s.%s" % (instance.vid, "license", extension)


def upload_rental_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s.%s" % (instance.vid, "rental", extension)


# Create your models here.
class Vendor(models.Model):
    vid = models.AutoField(primary_key=True)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    region = models.CharField(max_length=30, blank=True)
    linkman = models.CharField(max_length=20)
    cellphone = models.DecimalField(max_digits=11, decimal_places=0)
    logo = models.ImageField(upload_to=upload_logo_location)
    business_license = models.FileField(upload_to=upload_license_location)
    education_permit = models.FileField(upload_to=upload_permit_location, null=True, blank=True)
    rental_contract = models.FileField(upload_to=upload_rental_location, null=True, blank=True)

    isCertificated = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vid
