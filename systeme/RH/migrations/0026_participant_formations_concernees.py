# Generated by Django 5.0.3 on 2024-05-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0025_remove_participant_formation_concerne'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='formations_concernees',
            field=models.ManyToManyField(blank=True, related_name='participants_concernes', to='RH.formation'),
        ),
    ]
