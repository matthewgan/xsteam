from django.db import models


class Category(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
