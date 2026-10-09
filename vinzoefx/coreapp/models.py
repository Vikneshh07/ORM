from django.db import models
from django.contrib import admin
class blinkit(models.Model):
    Name=models.CharField(max_length=10)
    DoO=models.DateField(primary_key=True)
    Email=models.EmailField()
    Address=models.TextField()
    ordernumber=models.IntegerField()
    phonenumber=models.IntegerField()
    productreview=models.CharField(max_length=10)
    productnumber=models.IntegerField()
class blinkitAdmin(admin.ModelAdmin):
    list_display=["Name","DoO","Email","Address","ordernumber","phonenumber","productreview","productnumber"]


