from django import forms
from django.core.exceptions import ValidationError
from django.utils.dateformat import format
from django.utils.translation import gettext_lazy as _

from .models import Player, COUNTRY_CHOICES, GENDER_CHOICES
import imghdr
import datetime


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'alias', 'gender', 'date_of_birth', 'nationality', 'ranking', 'photo']
        labels = {
            'first_name': _('Nombre'),
            'last_name': _('Apellido'),
            'alias': _('Apodo'),
            'gender': _('Sexo'),
            'date_of_birth': _('Fecha de nacimiento'),
            'nationality': _('Nacionalidad'),
            'ranking': _('Ranking'),
            'photo': _('Foto'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'alias': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}, choices=GENDER_CHOICES),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'nationality': forms.Select(attrs={'class': 'form-control'}, choices=COUNTRY_CHOICES),
            'ranking': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Initial Ranking Points'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            if self.instance.date_of_birth:
                self.fields['date_of_birth'].initial = self.instance.date_of_birth.strftime('%Y-%m-%d')
            self.fields['gender'].initial = self.instance.gender

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            # Ensure photo is a valid image
            image_type = imghdr.what(photo)
            if image_type not in ['jpeg', 'png']:
                raise ValidationError("Unsupported file type. Please upload a JPEG or PNG image.")
        return photo
