# ttranking/matches/forms.py
from django import forms
from .models import SinglesMatch, DoublesMatch
from players.models import Player


class SinglesMatchForm(forms.ModelForm):
    class Meta:
        model = SinglesMatch
        fields = ['date', 'player1', 'player2', 'player1_score', 'player2_score', 'winner']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'player1': forms.Select(attrs={'class': 'form-control'}),
            'player2': forms.Select(attrs={'class': 'form-control'}),
            'player1_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'player2_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'winner': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player1'].queryset = Player.objects.all().order_by('ranking')
        self.fields['player2'].queryset = Player.objects.all().order_by('ranking')

        if self.instance and self.instance.pk:
            # Only show the players involved in the match as potential winners
            self.fields['winner'].queryset = Player.objects.filter(
                id__in=[self.instance.player1.id, self.instance.player2.id]
            )
        else:
            self.fields['winner'].queryset = Player.objects.none()


class DoublesMatchForm(forms.ModelForm):
    class Meta:
        model = DoublesMatch
        fields = ['date', 'team1_player1', 'team1_player2', 'team2_player1', 'team2_player2', 'team1_score', 'team2_score', 'winner_team']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'team1_player1': forms.Select(attrs={'class': 'form-control'}),
            'team1_player2': forms.Select(attrs={'class': 'form-control'}),
            'team2_player1': forms.Select(attrs={'class': 'form-control'}),
            'team2_player2': forms.Select(attrs={'class': 'form-control'}),
            'team1_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'team2_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'winner_team': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtering out the winner_team to be either 'Team1' or 'Team2' based on the players in the teams
        if 'team1_player1' in self.data and 'team1_player2' in self.data and 'team2_player1' in self.data and 'team2_player2' in self.data:
            self.fields['winner_team'].choices = [('Team1', 'Team 1'), ('Team2', 'Team 2')]
        else:
            self.fields['winner_team'].choices = [('', 'Select Team')]

        # Ensure team members are distinct
        self.fields['team1_player1'].queryset = Player.objects.all().order_by('ranking')
        self.fields['team1_player2'].queryset = Player.objects.all().order_by('ranking')
        self.fields['team2_player1'].queryset = Player.objects.all().order_by('ranking')
        self.fields['team2_player2'].queryset = Player.objects.all().order_by('ranking')
