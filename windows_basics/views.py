# home/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'windows_basics/index.html')
