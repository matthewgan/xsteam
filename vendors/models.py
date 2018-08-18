import uuid
from django.db import models


def upload_logo_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s.%s" % (instance.vid, "logo", extension)


# Create your models here.
class Vendor(models.Model):
    vid = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    region = models.CharField(max_length=30, blank=True)
    linkman = models.CharField(max_length=20)
    cellphone = models.DecimalField(max_digits=11, decimal_places=0)
    logo = models.ImageField(upload_to=upload_logo_location)
    isCertificated = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
