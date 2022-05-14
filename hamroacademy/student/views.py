from urllib import request
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse
from django.core import serializers
# from django.views.decorators.csrf import csrf_exempt
# # Create your views here.
# @csrf_exempt

def home(request):
     form = StudentRegistration()
     stud = User.objects.all()
     return render(request,'student/home.html',{'form':form,'stu':stud})
     

def save_data(request):
     if request.method == "POST":
          form =StudentRegistration(request.POST)
          if form.is_valid():
           name= request.POST['name']
           email= request.POST['email']
           password= request.POST['password']
           usr= User(name=name, email=email, password=password)
           usr.save()
           stud =User.objects.values()
           print(stud)
           student_data =list(stud)
           return JsonResponse({'status':'Save',
           'student_data':student_data})
          else:
           return JsonResponse({'status':0})


def postFriend(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
      form =StudentRegistration(request.POST)
      if form.is_valid():
            instance = form.save()
          
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
      else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)
   