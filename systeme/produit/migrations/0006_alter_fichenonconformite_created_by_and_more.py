# Generated by Django 5.0.3 on 2024-05-29 20:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0005_alter_nonconformite_niveau_gravite_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichenonconformite',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creer_fiche_nonConformite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nonconformite',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creer_nonConformite', to=settings.AUTH_USER_MODEL),
        ),
    ]
