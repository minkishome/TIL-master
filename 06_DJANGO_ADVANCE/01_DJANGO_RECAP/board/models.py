from django.db import models
from django.urls import reverse


class Article(models.Model):
    #id = models.IntegerField(primary_key=)
    title = models.CharField(max_length=100, null = False)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("board:article_detail", kwargs={"article_id": self.id})

class Comment(models.Model):
    content = models.CharField(max_length=1)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)