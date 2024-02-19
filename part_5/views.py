# home/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'part_5/index.html')
