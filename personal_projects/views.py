# home/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'personal_projects/index.html')