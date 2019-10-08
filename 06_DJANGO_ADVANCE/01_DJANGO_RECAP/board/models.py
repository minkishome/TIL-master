from django.db import models
from django.urls import reverse


class Article(models.Model):
    #id = models.IntegerField(primary_key=)
    title = models.CharField(max_length=100, null = False)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("board:detail", kwargs={"id": self.id})
    