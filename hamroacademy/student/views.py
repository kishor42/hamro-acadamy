from urllib import request
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse
from django.core import serializers
from django.views import View
from django.views.decorators.csrf import csrf_exempt
# # Create your views here.
@csrf_exempt

def home(request):
     form = StudentRegistration()
     stud = User.objects.all()
     return render(request,'student/home.html',{'form':form,'stu':stud})
     

def save_data(request):
     if request.method == "POST":
          form =StudentRegistration(request.POST)
          if form.is_valid():
           sid= request.POST.get('stuid')
           name= request.POST['name']
           email= request.POST['email']
           password= request.POST['password']
           if(sid==''):
            usr= User(name=name, email=email, password=password)
           else:
            usr= User(id=sid,name=name, email=email, password=password)
           usr.save()
           stud =User.objects.values()
          #  print(stud)
           student_data =list(stud)
           return JsonResponse({'status':'Save',
           'student_data':student_data})
          else:
           return JsonResponse({'status':0})

def delete_data(request):
     if request.method == "POST":
      id=request.POST.get('sid');
      pi=User.objects.get(pk=id)
      pi.delete();
      return JsonResponse({'status':1})
     else:
      return JsonResponse({'status':0})

def edit_data(request):
     if request.method == "POST":
      id=request.POST.get('sid');
      pi=User.objects.get(pk=id)
      print(pi)
      student_data={"id":pi.id,"name":pi.name,"email":pi.email,"password":pi.password}
      return JsonResponse(student_data)


def login (request):
 return render(request,'student/login.html')


def design (request):
 return render(request,'student/design.html')


def list_data(request):
    if request.method == "GET":
          stud =User.objects.all()
          #print(stud)
          student_data =serializers.serialize('json',stud)
          return JsonResponse(student_data,safe=False)
    return JsonResponse({'message':'wrongvalidation'})
   