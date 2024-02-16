from django.shortcuts import render

# In cybersecurity/views.py
def cybersecurity_index(request):
    return render(request, 'cybersecurity/index.html')
