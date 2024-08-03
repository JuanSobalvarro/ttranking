# ttranking/players/forms.py
from django import forms
from django.core.exceptions import ValidationError
import imghdr

from .models import Player, COUNTRY_CHOICES


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'date_of_birth', 'nationality', 'ranking', 'photo']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nationality': forms.Select(attrs={'class': 'form-control'}, choices=COUNTRY_CHOICES),
            'ranking': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Initial Ranking Points'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            # Ensure photo is a valid image
            image_type = imghdr.what(photo)
            if image_type not in ['jpeg', 'png']:
                raise ValidationError("Unsupported file type. Please upload a JPEG or PNG image.")
        return photo

