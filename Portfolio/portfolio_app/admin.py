from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AdditionalPage, Framework, Language, PageInfo, Project

admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(PageInfo)
admin.site.register(AdditionalPage)