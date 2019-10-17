from django.db import models
from django.urls import reverse
from django.conf import settings


class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    icon = models.CharField(max_length=30, default= '')
    image = models.ImageField(blank=True) # pip install pillow
    create_at = models.DateTimeField(auto_now_add= True) # auto_now_add는 처음 add 될때만 날짜가 삽입
    update_at = models.DateTimeField(auto_now=True) # auto_now는 수정이 될때마다
    class Meta:
        ordering = ['-create_at', ] # create_at 을 descending 내림차순으로 정렬

    #Detail 페이지를 쓸거라면 만들어요.
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})
    

    def __str__(self):
        return f'{self.pk}: {self.content[:10]}'

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name= 'comments')
    content = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-create_at', ] # create_at 을 descending 내림차순으로 정렬

    def __str__(self):
        return f'{self.pk}: {self.content[:10]}'