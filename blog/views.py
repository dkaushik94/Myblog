from django.shortcuts import render
from blog.models import *
from django.http import HttpResponse
# Create your views here.

def blogpage():
  b=blog.objects.all()
  
