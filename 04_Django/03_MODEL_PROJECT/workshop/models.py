from django.db import models

# Create your models here.

class Workshop(models.Model):
    name = models.CharField(max_length = 10)
    email = models.CharField(max_length = 10)
    birthday = models.DateField()
    age = models.IntergerField()

    def __str__(self):
        return f'{self.id} : {self.name}'