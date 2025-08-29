from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(null=False, max_length=16)
    phone = models.CharField(null=False, unique=True, max_length=11)

class Post(models.Model):
    title = models.CharField(null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

class
