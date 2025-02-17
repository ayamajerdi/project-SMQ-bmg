# Generated by Django 5.0.3 on 2024-04-21 13:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0003_historiqueversions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiqueversions',
            name='data',
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='created_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='fichier',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='libelle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='liste_informee',
            field=models.ManyToManyField(related_name='documentsInterne_informes_h', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='selection_activite',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='doc.activite'),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='selection_approbateur',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents_approuves_h', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='selection_redacteur',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents_rediges_h', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='selection_site',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='doc.site'),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='selection_verificateur',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents_verifies_h', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='statut',
            field=models.CharField(choices=[('En attente', 'En attente'), ('En cours', 'En cours'), ('Approuvé', 'Approuvé'), ('Vérifié', 'Vérifié'), ('Rejeté', 'Rejeté')], default='En attente', max_length=20),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='doc.type_document'),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='historiqueversions',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documentInterne_updated_h', to=settings.AUTH_USER_MODEL),
        ),
    ]
