from django.shortcuts import render
from .models import Post

def login(request):
    return render(request, 'login/login.html')