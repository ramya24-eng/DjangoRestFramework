# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class News(models.Model):
    category = models.CharField(max_length=1000, null=True)
    source = models.CharField(max_length=800,null=True)
    author = models.CharField(max_length=1000,null=True)
    title = models.CharField(max_length=2000,null=True)
    description=models.TextField(null=True)
    url=models.URLField(blank=True,null=True)
    urltoimage=models.ImageField(upload_to ='img/')
    publishedat=models.DateTimeField(blank=True,null=True)
    content=models.TextField(null=True)

    def __str__(self):
        return self.title

