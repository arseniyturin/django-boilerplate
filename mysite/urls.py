from django.contrib import admin
from django.urls import path, re_path, include
from website import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('admin/', admin.site.urls),    
]
