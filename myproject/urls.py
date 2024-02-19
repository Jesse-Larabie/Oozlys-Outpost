from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Assuming your app is named 'home'
    path('cybersecurity/', include('cybersecurity.urls')),  # Assuming another app is named 'cybersecurity'
    path('part_1/', include('part_1.urls')),
    path('part_2/', include('part_2.urls')),
    path('part_3/', include('part_3.urls')),
    path('part_4/', include('part_4.urls')),
    path('part_5/', include('part_5.urls')),
    path('part_6/', include('part_6.urls')),
    path('part_7/', include('part_7.urls')),
    path('part_8/', include('part_8.urls')),
    path('personal_projects/', include('personal_projects.urls')),
    
]
