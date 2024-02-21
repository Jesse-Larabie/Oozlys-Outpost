# home/views.py
from django.shortcuts import render

def index_view(request):
    return render(request, 'home/index.html')  # Rendering the 'index.html' template

def home_view(request):
    return render(request, 'home/index.html')  # Rendering the 'index.html' template
