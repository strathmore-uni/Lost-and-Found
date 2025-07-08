from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
]
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("register.html")


    

