from django.db import models


class Article(models.Model):
    #id = models.IntegerField(primary_key=)
    title = models.CharField(max_length=100, null = False)
    content = models.TextField()

