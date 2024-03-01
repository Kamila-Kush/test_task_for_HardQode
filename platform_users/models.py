from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(
        to=User,
        null=True, blank=False,
        on_delete=models.SET_NULL,
    )
    name = models.CharField(max_length=255, verbose_name='Имя', default='Somebody')

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(
        to=User,
        null=True, blank=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, verbose_name='Имя')
    access = models.BooleanField()

    def __str__(self):
        return self.name



