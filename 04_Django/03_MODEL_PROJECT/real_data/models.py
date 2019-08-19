from django.db import models

# Create your models here.

class HotIssue(models.Model):
    date = models.CharField(max_length = 100)
    time = models.CharField(max_length = 100)
    rank = models.IntegerField()
    keyword = models.CharField(max_length = 100)


