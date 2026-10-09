# Ex02 Django ORM Web Application
## Date: 09.10.2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import blinkit,blinkitAdmin
admin.site.register(blinkit,blinkitAdmin)


```


## OUTPUT
![alt text](<Screenshot 2026-10-09 135901.png>)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
