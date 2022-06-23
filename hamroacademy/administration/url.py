
from django.contrib import admin
from django.urls import path
from administration import views


urlpatterns = [
   path('adminmain/',views.adminmain,name='adminmain'),
   path('adminabout/',views.adminabout,name='adminabout'),

 
]