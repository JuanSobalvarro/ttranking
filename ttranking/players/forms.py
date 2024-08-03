# ttranking/players/forms.py
from django import forms
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
