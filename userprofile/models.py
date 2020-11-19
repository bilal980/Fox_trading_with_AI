from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=40)
    gender=models.CharField(max_length=10)
    time=models.DateTimeField(auto_now=True)
