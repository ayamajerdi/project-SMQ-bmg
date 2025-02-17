# Generated by Django 5.0.3 on 2024-04-22 11:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='fichecloturenonconformite',
            name='created_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='fichecloturenonconformite',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creer_ficheC_nonConformite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fichecloturenonconformite',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='fichecloturenonconformite',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modifier_ficheC_nonConformite', to=settings.AUTH_USER_MODEL),
        ),
    ]
