from django.shortcuts import render

def cybersecurity_view(request):
    #view logic here
    return render(request, 'cybersecurity/index.html')  # Replace 'index.html' with your actual template
