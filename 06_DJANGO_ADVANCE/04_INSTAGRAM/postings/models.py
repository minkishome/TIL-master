from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

User = get_user_model()
class HashTag(TimeStampedModel):
    content = models.CharField(max_length=20)

# Create your models here.
class Posting(TimeStampedModel):
    like_users = models.ManyToManyField(User, related_name='like_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postings')
    content = models.CharField(max_length=140)
    hastags = models.ManyToManyField(HashTag, blank=True, related_name='postings')

    class Meta:
        ordering = ('-created', )

    def get_absolute_url(self):
        return reverse("posting:posting_detail", kwargs={"posting_id": self.pk})
        

class Image(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='Image')
    file = ProcessedImageField(
        processors=[ResizeToFill(600,600)],
        upload_to='posting/images',
        format='JPEG',
        options={'quality':90},
    )

class Comment(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=140)

