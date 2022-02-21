from urllib import request
import django
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request,'index.html')
