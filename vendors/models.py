import uuid
from django.db import models
from django.contrib.auth.models import User


def upload_logo_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s.%s" % (instance.company, "logo", extension)


def upload_permit_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s.%s" % (instance.company, "cert", extension)


def upload_license_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s.%s" % (instance.company, "license", extension)


def upload_rental_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s.%s" % (instance.company, "rental", extension)


# Create your models here.
class Vendor(models.Model):
    vid = models.AutoField(primary_key=True)
    company = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    region = models.CharField(max_length=30, blank=True)
    linkman = models.CharField(max_length=20, blank=True)
    cellphone = models.DecimalField(max_digits=11, decimal_places=0, default=0)
    logo = models.ImageField(upload_to=upload_logo_location ,null=True)
    business_license = models.FileField(upload_to=upload_license_location, null=True)
    education_permit = models.FileField(upload_to=upload_permit_location, null=True, blank=True)
    rental_contract = models.FileField(upload_to=upload_rental_location, null=True, blank=True)

    isCertificated = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    authUser = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.company

    class Meta:
        verbose_name = '合作机构'
        verbose_name_plural = '合作机构'
