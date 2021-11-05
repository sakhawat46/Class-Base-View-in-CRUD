from django import forms
from django.core import validators
from django.forms import fields
from first_app import models

class MusicianFrom(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget = forms.TextInput(attrs = {'type':'date'}))
    class Meta:
        model = models.Album
        fields = '__all__'
