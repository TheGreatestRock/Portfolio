# portfolio/models.py
from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    entreprise = models.ForeignKey('Entreprise', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    frameworks = models.ManyToManyField(Framework, blank=True)
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Entreprise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='entreprise_images/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Bio(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    skills = models.JSONField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    social_links = models.JSONField()

    def __str__(self):
        return self.name