from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.
def home(request):

    return render(request, 'index.html')

def team(request):

    return render(request, 'team.html')

def gallery(request):

    return render(request, 'gallery.html')
