from django.db import models
from datetime import datetime


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at=models.DateTimeField(default=datetime.now, blank=True)
class employee(models.Model):
    empname=models.CharField(max_length=100)
    empjoindate=models.DateTimeField()
class client(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    telephone=models.CharField(max_length=150)
    appointment__date=models.DateTimeField()
