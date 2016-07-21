from django.db import models
from django.contrib import admin
# Create your models here.

class Visitor(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    mobile_no=models.IntegerField()
    company=models.CharField(max_length=200)
    visiting=models.CharField(max_length=100)

    def __str__(self):
        return self.name

