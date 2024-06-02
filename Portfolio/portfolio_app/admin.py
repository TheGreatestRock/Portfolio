from django.contrib import admin

# Register your models here.
from .models import Bio, Entreprise, Framework, Language, Project
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget



class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('languages', 'frameworks')

class BioAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

admin.site.register(Project, ProjectAdmin)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Entreprise)
admin.site.register(Bio, BioAdmin)






