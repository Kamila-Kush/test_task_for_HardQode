from django.db import models
from platform_users.models import Author, Student

class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название курса", blank=False)
    author = models.ForeignKey(
        to=Author,
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name='course'
    )
    min_students = models.IntegerField(verbose_name='Минимальное количество учащихся')
    max_students = models.IntegerField(verbose_name='Максимальное количество учащихся')
    start_date = models.DateTimeField(verbose_name='Дата и время запуска курса')
    price = models.IntegerField(verbose_name='Стоимость курса')

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название урока", blank=False)
    course = models.ForeignKey(
        to=Course,
        null=True, blank=False,
        on_delete=models.CASCADE,
        related_name='lesson'
    )
    video_link = models.CharField(max_length=255, blank=False)

class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название группы')
    course = models.ForeignKey(
        to=Course,
        related_name='group',
        on_delete=models.CASCADE
    )
    student = models.ManyToManyField(
        to=Student,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name



