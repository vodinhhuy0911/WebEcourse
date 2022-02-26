from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
#
# class User(AbstractUser):
#     avatar = models.ImageField(upload_to='/uploads/%Y/%m')

class Category (models.Model):
    name = models.CharField(max_length= 100,null = False, unique=True)
    def __str__(self):
        return self.name

class MultipleChoice(models.Model):
    content = models.TextField(null=False)
    correctAnswer = models.TextField(null=False)
    answers = models.ManyToManyField("Answer",)
    def __str__(self):
        return self.content

class Answer(models.Model):
    name = models.TextField(null=False)
    def __str__(self):
        return self.answer