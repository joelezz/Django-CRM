from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request): 
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')