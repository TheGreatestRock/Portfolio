import json
from django.shortcuts import redirect, render, get_object_or_404

from portfolio_app.forms import TextFieldForm
from .models import ApprentissageCritique, Bio, Competence, GlossaryTerm, Project, TextField

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def about(request):
    bio = Bio.objects.first()
    projects = Project.objects.all()
    
    context = {
        'profile_picture_url': bio.profile_picture.url if bio and bio.profile_picture else None,
        'name': bio.name if bio else None,
        'bio': bio.bio if bio else None,
        'email': bio.email if bio else None,
        'skills': bio.skills if bio else None,
        'social_links': bio.social_links if bio else None,
        'projects': projects
    }
    
    return render(request, 'portfolio/about.html', context)

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/all_projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    projects = Project.objects.all()
    text_fields = TextField.objects.filter(project=project)
    all_competences = Competence.objects.all()
    all_apprentissages = ApprentissageCritique.objects.all()
    
    all_glossary_terms = []
    #glossary terms have a term field
    for term in GlossaryTerm.objects.all():
        all_glossary_terms.append(term.term)
    
    glossary_terms = GlossaryTerm.objects.all()

    context = {
        'project': project,
        'projects' : projects,
        'text_fields': text_fields,
        'all_competences': all_competences,
        'all_apprentissages': all_apprentissages,
        'glossary_terms': glossary_terms,
        'all_glossary_terms': json.dumps(all_glossary_terms)
    }
    return render(request, 'portfolio/project_detail.html', context)

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