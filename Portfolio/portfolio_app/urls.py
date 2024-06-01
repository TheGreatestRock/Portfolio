# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/<int:pk>/', views.page_detail, name='page_detail'), 
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]
