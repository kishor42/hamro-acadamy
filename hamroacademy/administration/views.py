from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views import View

# Create your views here.


def adminmain (request):
    
 return render(request,'administration/adminmain.html')

 
def adminabout (request):
 return render(request,'administration/adminabout.html')