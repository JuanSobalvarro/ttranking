# Generated by Django 5.1.2 on 2025-01-21 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
        ('players', '0002_alter_player_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doublesmatch',
            name='team1_score',
        ),
        migrations.RemoveField(
            model_name='doublesmatch',
            name='team2_score',
        ),
        migrations.RemoveField(
            model_name='doublesmatch',
            name='winner_team',
        ),
        migrations.RemoveField(
            model_name='singlesmatch',
            name='player1_score',
        ),
        migrations.RemoveField(
            model_name='singlesmatch',
            name='player2_score',
        ),
        migrations.AddField(
            model_name='doublesmatch',
            name='winner_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doubles_matches_won1', to='players.player'),
        ),
        migrations.AddField(
            model_name='doublesmatch',
            name='winner_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doubles_matches_won2', to='players.player'),
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
