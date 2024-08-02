# ttranking/matches/forms.py
from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['match_type', 'date', 'player1', 'player2', 'team1', 'team2', 'score', 'winner']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'score': forms.TextInput(attrs={'placeholder': 'e.g., 3-2'}),
        }
