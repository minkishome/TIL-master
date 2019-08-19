from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)
    github_id = models.CharField(max_length = 50)
    age = models.IntegerField()

class Menus(models.Model):
    name = models.CharField(max_length = 10)
    price = models.FloatField()
    category = models.CharField(max_length = 10)
 

