import json
from django.shortcuts import redirect, render, get_object_or_404

from portfolio_app.forms import TextFieldForm
from .models import Bio, Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def about(request):
    bio = Bio.objects.first()  # Assuming there's only one Bio entry
    projects = Project.objects.all()
    context = {
        'name': bio.name,
        'bio': bio.bio,
        'email': bio.email,
        'skills': bio.skills,
        'profile_picture_url': bio.profile_picture.url,
        'social_links': bio.social_links,
        'projects': projects
    }
    return render(request, 'portfolio/about.html', context)

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/all_projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    text_fields = project.text_fields.all() 
    glossary_terms_dict = {} 
    for text_field in text_fields:
        glossary_terms_dict.update({term.term: term.description for term in text_field.glossary_terms.all()})
    glossary_terms_dict = json.dumps(glossary_terms_dict)
    return render(request, 'portfolio/project_detail.html', {'project': project, 'text_fields': text_fields, 'glossary_terms_dict': glossary_terms_dict})

def add_text_field(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        text_field_form = TextFieldForm(request.POST, request.FILES)
        if text_field_form.is_valid():
            text_field = text_field_form.save(commit=False)
            text_field.project = project
            text_field.save()
            text_field_form.save_m2m()  # Save the many-to-many relationships
            return redirect('project_detail', project_id=project.id)
    else:
        text_field_form = TextFieldForm()

    return render(request, 'add_text_field.html', {'form': text_field_form, 'project': project})