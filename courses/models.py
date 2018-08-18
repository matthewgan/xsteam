import datetime
from django.db import models
from categories.models import Category
from vendors.models import Vendor


def upload_showcase_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s.%s" % (instance.vendor.vid, instance.cid, extension)


# Create your models here.
class Course(models.Model):
    cid = models.AutoField(primary_key=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="course")
    name = models.CharField(max_length=30, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="vendor")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    club_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_note = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=100, default="请简介上线课程")
    description = models.CharField(max_length=1000, blank=True)
    detail = models.CharField(max_length=5000, blank=True)
    showcase = models.ImageField("showcases", upload_to=upload_showcase_location)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    expire = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.cid
