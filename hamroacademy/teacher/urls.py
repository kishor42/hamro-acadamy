from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]