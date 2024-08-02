# ttranking/matches/forms.py
from django import forms
from .models import SinglesMatch, DoublesMatch
from players.models import Player


class SinglesMatchForm(forms.ModelForm):
    class Meta:
        model = SinglesMatch
        fields = ['date', 'player1', 'player2', 'score', 'winner']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'player1': forms.Select(attrs={'class': 'form-control'}),
            'player2': forms.Select(attrs={'class': 'form-control'}),
            'score': forms.TextInput(attrs={'class': 'form-control'}),
            'winner': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally, customize player choices if needed
        self.fields['player1'].queryset = Player.objects.all().order_by('ranking')
        self.fields['player2'].queryset = Player.objects.all().order_by('ranking')
        self.fields['winner'].queryset = Player.objects.all().order_by('ranking')


class DoublesMatchForm(forms.ModelForm):
    class Meta:
        model = DoublesMatch
        fields = ['date', 'team1_player1', 'team1_player2', 'team2_player1', 'team2_player2', 'score', 'winner_team']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'team1_player1': forms.Select(attrs={'class': 'form-control'}),
            'team1_player2': forms.Select(attrs={'class': 'form-control'}),
            'team2_player1': forms.Select(attrs={'class': 'form-control'}),
            'team2_player2': forms.Select(attrs={'class': 'form-control'}),
            'score': forms.TextInput(attrs={'class': 'form-control'}),
            'winner_team': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally, customize player choices if needed
        self.fields['team1_player1'].queryset = Player.objects.all().order_by('ranking')
        self.fields['team1_player2'].queryset = Player.objects.all().order_by('ranking')
        self.fields['team2_player1'].queryset = Player.objects.all().order_by('ranking')
        self.fields['team2_player2'].queryset = Player.objects.all().order_by('ranking')
