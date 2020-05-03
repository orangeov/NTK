from django.urls import path

from . import views

urlpatterns = [
    path('', views.professional_create_view, name = 'professional_create_view'),
    
    ]