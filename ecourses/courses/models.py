from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
#
# class User(AbstractUser):
#     avatar = models.ImageField(upload_to='/uploads/%Y/%m')

class Category (models.Model):
    name = models.CharField(max_length= 100,null = False, unique=True)

class MultipleChoice(models.Model):
    content = models.TextField(null=False)
    correctAnswer = models.TextField(null=False)

class Answer(models.Model):
    answer = models.TextField(null=False)
    multipleChoice = models.ForeignKey(MultipleChoice,on_delete= models.SET_NULL, null=True)