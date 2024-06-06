from django import forms
from .models import TextField, Image

class TextFieldForm(forms.ModelForm):
    class Meta:
        model = TextField
        fields = ['content', 'images', 'competences', 'apprentissages_critiques']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
