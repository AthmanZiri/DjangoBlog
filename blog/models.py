# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here

from django.db import models

class Tag(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255, null=True, default='')

    def __str__(self):
        return self.name

class blog(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField(max_length=20000)
    tags=models.ManyToManyField(Tag)
 
    def __str__(self):
        return self.title


