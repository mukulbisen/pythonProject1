from django.db import models

# Create your models here.
class Employee(models.Model):
    Bookname = models.CharField(max_length=100)
    Authorname = models.CharField(max_length=100)
    Content_type = models.CharField(max_length=100)
