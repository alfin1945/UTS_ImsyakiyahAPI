from django.contrib import admin
# from django.urls import path
from django.urls import path, include
from . import views 

urlpatterns = [
    path ('home/', views.index),
    path ('coba/', views.coba),
    path ('', include('jadwal.urls')),
    path('admin/', admin.site.urls),
]
