# ttranking/players/forms.py
from django import forms
from django.core.exceptions import ValidationError
import imghdr

from players.models import Player, COUNTRY_CHOICES
from matches.models import SinglesMatch, DoublesMatch

import datetime


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'alias', 'date_of_birth', 'nationality', 'ranking', 'photo']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'alias': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nationality': forms.Select(attrs={'class': 'form-control'}, choices=COUNTRY_CHOICES),
            'ranking': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Initial Ranking Points'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial value for date_of_birth
        if self.instance and self.instance.pk:
            self.fields['photo'].initial = self.instance.photo
            # self.fields['date_of_birth'].initial = self.instance.date_of_birth

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            # Ensure photo is a valid image
            image_type = imghdr.what(photo)
            if image_type not in ['jpeg', 'png']:
                raise ValidationError("Unsupported file type. Please upload a JPEG or PNG image.")
        return photo


class SinglesMatchForm(forms.ModelForm):
    class Meta:
        model = SinglesMatch
        fields = ['date', 'player1', 'player1_score', 'player2', 'player2_score']
        labels = ['Fecha y Hora']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'player1': forms.Select(attrs={'class': 'form-control'}),
            'player1_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'player2': forms.Select(attrs={'class': 'form-control'}),
            'player2_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = datetime.datetime.now().replace(second=0, microsecond=0)
        self.fields['player1'].queryset = Player.objects.all().order_by('first_name')
        self.fields['player2'].queryset = Player.objects.all().order_by('first_name')

    def clean(self):
        cleaned_data = super().clean()
        player1 = cleaned_data.get('player1')
        player2 = cleaned_data.get('player2')

        if player1 == player2:
            raise forms.ValidationError("Player 1 and Player 2 cannot be the same.")

        return cleaned_data


class DoublesMatchForm(forms.ModelForm):
    class Meta:
        model = DoublesMatch
        fields = ['date', 'team1_player1', 'team1_player2', 'team1_score', 'team2_player1', 'team2_player2', 'team2_score']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'team1_player1': forms.Select(attrs={'class': 'form-control'}),
            'team1_player2': forms.Select(attrs={'class': 'form-control'}),
            'team1_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'team2_player1': forms.Select(attrs={'class': 'form-control'}),
            'team2_player2': forms.Select(attrs={'class': 'form-control'}),
            'team2_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = datetime.datetime.now().replace(second=0, microsecond=0)
        # Ensure team members are distinct
        self.fields['team1_player1'].queryset = Player.objects.all().order_by('first_name')
        self.fields['team1_player2'].queryset = Player.objects.all().order_by('first_name')
        self.fields['team2_player1'].queryset = Player.objects.all().order_by('first_name')
        self.fields['team2_player2'].queryset = Player.objects.all().order_by('first_name')

    def clean(self):
        cleaned_data = super().clean()
        team1_player1 = cleaned_data.get('team1_player1')
        team1_player2 = cleaned_data.get('team1_player2')
        team2_player1 = cleaned_data.get('team2_player1')
        team2_player2 = cleaned_data.get('team2_player2')

        if team1_player1 == team1_player2:
            raise forms.ValidationError("Team 1 players cannot be the same.")
        if team2_player1 == team2_player2:
            raise forms.ValidationError("Team 2 players cannot be the same.")
        all_players = {team1_player1, team1_player2, team2_player1, team2_player2}
        if len(all_players) < 4:
            raise forms.ValidationError("Players cannot be repeated across teams.")

        return cleaned_data
