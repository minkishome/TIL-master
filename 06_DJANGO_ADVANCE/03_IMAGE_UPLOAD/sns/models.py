from django.db import models
from django.urls import reverse


class Posting(models.Model):
    content = models.TextField()
    icon = models.CharField(max_length=30, default= '')
    image = models.ImageField(blank=True) # pip install pillow
    create_at = models.DateTimeField(auto_now_add= True) # auto_now_add는 처음 add 될때만 날짜가 삽입
    update_at = models.DateTimeField(auto_now=True) # auto_now는 수정이 될때마다


    #Detail 페이지를 쓸거라면 만들어요.
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})
    

    def __str__(self):
        return f'{self.pk}: {self.content[:10]}'