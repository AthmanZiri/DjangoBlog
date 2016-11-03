# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import blog

# Create your views here.

from django.http import HttpResponse 
    
def post_list(request):
    posts = blog.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})   
    

