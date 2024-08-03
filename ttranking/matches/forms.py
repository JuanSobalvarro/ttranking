# ttranking/matches/forms.py
from django import forms
from .models import SinglesMatch, DoublesMatch
from players.models import Player


class SinglesMatchForm(forms.ModelForm):
    class Meta:
        model = SinglesMatch
        fields = ['date', 'player1', 'player2', 'player1_score', 'player2_score']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'player1': forms.Select(attrs={'class': 'form-control'}),
            'player2': forms.Select(attrs={'class': 'form-control'}),
            'player1_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'player2_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player1'].queryset = Player.objects.all().order_by('ranking')
        self.fields['player2'].queryset = Player.objects.all().order_by('ranking')

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
        fields = ['date', 'team1_player1', 'team1_player2', 'team2_player1', 'team2_player2', 'team1_score', 'team2_score']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'team1_player1': forms.Select(attrs={'class': 'form-control'}),
            'team1_player2': forms.Select(attrs={'class': 'form-control'}),
            'team2_player1': forms.Select(attrs={'class': 'form-control'}),
            'team2_player2': forms.Select(attrs={'class': 'form-control'}),
            'team1_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'team2_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure team members are distinct
        self.fields['team1_player1'].queryset = Player.objects.all().order_by('ranking')
        self.fields['team1_player2'].queryset = Player.objects.all().order_by('ranking')
        self.fields['team2_player1'].queryset = Player.objects.all().order_by('ranking')
        self.fields['team2_player2'].queryset = Player.objects.all().order_by('ranking')

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
