import datetime
from django.db import models
from categories.models import Category
from vendors.models import Vendor


def upload_showcase_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s.%s" % (instance.vendor.company, "showcase", extension)


# Create your models here.
class Course(models.Model):
    cid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, default="xxx")
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="course")
    name = models.CharField(max_length=30, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="vendor")
    price = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    tag1 = models.CharField(max_length=10, blank=True)
    tag2 = models.CharField(max_length=10, blank=True)
    tag3 = models.CharField(max_length=10, blank=True)
    like = models.CharField(max_length=5, blank=True)
    club_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_note = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=100, default="请简介上线课程")
    description = models.CharField(max_length=1000, blank=True)
    detail = models.CharField(max_length=5000, blank=True)
    showcase = models.ImageField("showcases", upload_to=upload_showcase_location)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    service = models.CharField(max_length=100, default="可退货")
    review_point = models.CharField(max_length=5, default="4.0")
    review_number = models.CharField(max_length=5, default="0")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'
