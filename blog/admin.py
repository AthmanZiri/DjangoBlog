# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django import forms
from blog.models import blog, Tag

admin.site.register(blog)
admin.site.register(Tag)
