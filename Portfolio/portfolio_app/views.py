from django.shortcuts import render, get_object_or_404
from .models import Bio, Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def about(request):
    bio = Bio.objects.first()  # Assuming there's only one Bio entry
    context = {
        'name': bio.name,
        'bio': bio.bio,
        'email': bio.email,
        'skills': bio.skills,
        'profile_picture_url': bio.profile_picture.url,
        'social_links': bio.social_links,
    }
    return render(request, 'portfolio/about.html', context)

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/all_projects.html', {'projects': projects})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    projects = Project.objects.all()
    return render(request, 'portfolio/project_detail.html', {'project': project}, {'projects': projects})