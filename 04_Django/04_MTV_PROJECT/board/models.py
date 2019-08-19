from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 10)
    content = models.CharField(max_length = 10)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now= True)


    def __str__(self):
        return f'{self.id} : {self.title}'
    



        