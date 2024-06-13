from django.contrib import admin
from django.forms import JSONField
from .models import Language, Framework, Project, Competence, ApprentissageCritique, TextField, Image, Entreprise, Bio, GlossaryTerm
from django_json_widget.widgets import JSONEditorWidget

# Registering the models for the admin interface
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'entreprise', 'supervisor', 'referent_teacher')
    list_filter = ('entreprise', 'languages', 'frameworks')
    search_fields = ('title', 'description')
    filter_horizontal = ('languages', 'frameworks')

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ApprentissageCritique)
class ApprentissageCritiqueAdmin(admin.ModelAdmin):
    list_display = ('title', 'competence')
    list_filter = ('competence',)
    search_fields = ('title', 'description')

@admin.register(TextField)
class TextFieldAdmin(admin.ModelAdmin):
    list_display = ('project', 'content')
    list_filter = ('project', 'competences', 'apprentissages_critiques')
    search_fields = ('content',)
    filter_horizontal = ('competences', 'apprentissages_critiques', 'glossary_terms', 'images')

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    list_display = ('name', 'email')
    search_fields = ('name', 'email', 'bio')

@admin.register(GlossaryTerm)
class GlossaryTermAdmin(admin.ModelAdmin):
    list_display = ('term', 'description')
    search_fields = ('term', 'description')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description')
    search_fields = ('id', 'name', 'image', 'description')
