from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Entreprise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='entreprise_images/', blank=True, null=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Competence(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ApprentissageCritique(models.Model):
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE, related_name='apprentissages_critiques')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='text_field_images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

class GlossaryTerm(models.Model):
    term = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.term

class Project(models.Model):
    title = models.CharField(max_length=100)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    link = models.URLField(blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    frameworks = models.ManyToManyField(Framework, blank=True)
    github_link = models.URLField(blank=True)
    supervisor = models.CharField(max_length=100, blank=True)
    referent_teacher = models.CharField(max_length=100, blank=True)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.title

class TextField(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='text_fields')
    content = models.TextField()
    images = models.ManyToManyField(Image, blank=True)
    competences = models.ManyToManyField(Competence, blank=True)
    apprentissages_critiques = models.ManyToManyField(ApprentissageCritique, blank=True)
    glossary_terms = models.ManyToManyField(GlossaryTerm, blank=True)

    def __str__(self):
        return f"TextField for {self.project.title}"

class Bio(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    skills = models.JSONField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    social_links = models.JSONField()

    def __str__(self):
        return self.name
