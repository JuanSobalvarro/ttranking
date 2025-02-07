# Generated by Django 5.1.2 on 2025-02-07 03:37

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
        ('seasons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoublesMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doubles_matches', to='seasons.season')),
                ('team1_player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubles_matches_team1_player1', to='players.player')),
                ('team1_player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubles_matches_team1_player2', to='players.player')),
                ('team2_player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubles_matches_team2_player1', to='players.player')),
                ('team2_player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubles_matches_team2_player2', to='players.player')),
                ('winner_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doubles_matches_won1', to='players.player')),
                ('winner_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doubles_matches_won2', to='players.player')),
            ],
        ),
        migrations.CreateModel(
            name='DoublesGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1_score', models.IntegerField(default=0)),
                ('team2_score', models.IntegerField(default=0)),
                ('winner', models.IntegerField(blank=True, null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='matches.doublesmatch')),
            ],
        ),
        migrations.CreateModel(
            name='SinglesMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='singles_matches_as_player1', to='players.player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='singles_matches_as_player2', to='players.player')),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='singles_matches', to='seasons.season')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='singles_matches_won', to='players.player')),
            ],
        ),
        migrations.CreateModel(
            name='SinglesGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_score', models.IntegerField(default=0)),
                ('player2_score', models.IntegerField(default=0)),
                ('winner', models.IntegerField(blank=True, null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='matches.singlesmatch')),
            ],
        ),
    ]
