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
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    frameworks = models.ManyToManyField(Framework, blank=True)
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class PageInfo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class AdditionalPage(models.Model):
    page_info = models.ForeignKey(PageInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title