# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]
