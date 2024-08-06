# Generated by Django 5.0.7 on 2024-08-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_player_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=100),
            preserve_default=False,
        ),
    ]
