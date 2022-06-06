
from django.contrib import admin
from django.urls import path
from student import views


urlpatterns = [
   path('',views.home,name='home'),
    path('save/',views.save_data,name='save'),
    path('delete/',views.delete_data,name = "delete"),
    path('edit/',views.edit_data,name = "edit"),
    path('list/',views.list_data,name = "listdata"),
    path('login/',views.login, name='login' ),
]