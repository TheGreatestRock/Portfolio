from django.shortcuts import render, get_object_or_404
from .models import AdditionalPage, Project, PageInfo

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def about(request):
    # Fetch information from PageInfo model
    page_info = get_object_or_404(PageInfo, title="About Me")
    return render(request, 'portfolio/about.html', {'page_info': page_info})

def page_detail(request, pk):
    # Fetch information from PageInfo model
    page_info = get_object_or_404(PageInfo, pk=pk)
    additional_pages = AdditionalPage.objects.filter(page_info=page_info)
    return render(request, 'portfolio/page_detail.html', {'page_info': page_info, 'additional_pages': additional_pages})

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/all_projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})