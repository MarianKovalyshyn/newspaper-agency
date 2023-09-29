from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255)


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField()


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField()
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    publishers = models.ManyToManyField(Redactor)
