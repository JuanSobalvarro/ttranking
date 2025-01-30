# Generated by Django 5.1.2 on 2025-01-27 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_delete_ranking'),
        ('seasons', '0003_season_doubles_points_for_loss_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField(default=0)),
                ('matches_played', models.IntegerField(default=0)),
                ('victories', models.IntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season_rankings', to='players.player')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_rankings', to='seasons.season')),
            ],
            options={
                'unique_together': {('player', 'season')},
            },
        ),
    ]
