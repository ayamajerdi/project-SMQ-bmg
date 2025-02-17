# Generated by Django 5.0.3 on 2024-04-15 00:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lieu_Classement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LIEU_CLASSEMENT_CHOICES', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type_Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_de_document', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DocExt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('numerique', 'Numérique'), ('papier', 'Papier')], max_length=50)),
                ('designation', models.CharField(max_length=255)),
                ('duree_classement', models.CharField(max_length=100)),
                ('fichier', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('created_at', models.DateTimeField(default=None, null=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documentExterne_created', to=settings.AUTH_USER_MODEL)),
                ('liste_informee', models.ManyToManyField(related_name='documentsExterne_informes', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documentExterne_updated', to=settings.AUTH_USER_MODEL)),
                ('lieu_classement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.lieu_classement')),
            ],
        ),
        migrations.CreateModel(
            name='DocInt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255)),
                ('fichier', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('statut', models.CharField(choices=[('En attente', 'En attente'), ('En cours', 'En cours'), ('Approuvé', 'Approuvé'), ('Vérifié', 'Vérifié'), ('Rejeté', 'Rejeté')], default='En attente', max_length=20)),
                ('created_at', models.DateTimeField(default=None, null=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('liste_informee', models.ManyToManyField(related_name='documentsInterne_informes', to=settings.AUTH_USER_MODEL)),
                ('selection_activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.activite')),
                ('selection_approbateur', models.ForeignKey(limit_choices_to={'groups__name': 'approbateur'}, on_delete=django.db.models.deletion.CASCADE, related_name='documents_approuves', to=settings.AUTH_USER_MODEL)),
                ('selection_redacteur', models.ForeignKey(limit_choices_to={'groups__name': 'redacteur'}, on_delete=django.db.models.deletion.CASCADE, related_name='documents_rediges', to=settings.AUTH_USER_MODEL)),
                ('selection_verificateur', models.ForeignKey(limit_choices_to={'groups__name': 'verificateur'}, on_delete=django.db.models.deletion.CASCADE, related_name='documents_verifies', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documentInterne_updated', to=settings.AUTH_USER_MODEL)),
                ('selection_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.site')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.type_document')),
            ],
        ),
    ]
