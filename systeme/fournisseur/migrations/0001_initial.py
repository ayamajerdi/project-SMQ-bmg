# Generated by Django 5.0.3 on 2024-05-31 11:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CRM', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_fournisseur', models.CharField(max_length=50, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('raison_sociale', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=255)),
                ('numero_telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('categorie', models.CharField(choices=[('electronique', 'electronique'), ('textile', 'textile'), ('alimentation', 'alimentation')])),
                ('type_fournisseur', models.CharField(choices=[('Fournisseur de matière première', 'Fournisseur de matière première'), ('Fournisseur de composants', 'Fournisseur de composants'), ('Fournisseur de produits finis', 'Fournisseur de produits finis')])),
                ('fournisseur_agree', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=None, null=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('periodicite_evaluation', models.CharField(choices=[('annuelle', 'Annuelle'), ('semestrielle', 'Semestrielle'), ('trimestrielle', 'Trimestrielle')], max_length=20)),
                ('pieces_jointes', models.FileField(blank=True, null=True, upload_to='pieces_jointes_fournisseur/')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fournisseur_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fournisseur_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReclamationFournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=None, null=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('numero_sequentiel', models.CharField(max_length=50, unique=True)),
                ('date_reclamation', models.DateField()),
                ('description', models.TextField()),
                ('type_reclamation', models.CharField(choices=[('Service', 'Service'), ('Produit', 'Produit'), ('Facturation', 'Facturation'), ('Livraison', 'Livraison'), ('Support', 'Support')], default=None, max_length=50)),
                ('gravite', models.CharField(choices=[('faible', 'Faible'), ('moyenne', 'Moyenne'), ('élevée', 'Élevée')], max_length=10)),
                ('designation', models.CharField(max_length=100)),
                ('actions', models.TextField()),
                ('pieces_jointes', models.FileField(blank=True, null=True, upload_to='pieces_jointes_reclamation_fournisseur/')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reclamation_fournisseur_created', to=settings.AUTH_USER_MODEL)),
                ('fournisseur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fournisseur.fournisseur')),
                ('reclamation_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRM.reclamationclient')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reclamation_fournisseur_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationFournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=None, null=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('critere_evaluation', models.TextField()),
                ('notes', models.DecimalField(decimal_places=1, max_digits=3)),
                ('commentaires', models.TextField()),
                ('periodicite_evaluation', models.CharField(choices=[('annuelle', 'Annuelle'), ('semestrielle', 'Semestrielle'), ('trimestrielle', 'Trimestrielle'), ('mensuelle', 'Mensuelle'), ('ponctuelle', 'Ponctuelle')], max_length=20)),
                ('pieces_jointes', models.FileField(blank=True, null=True, upload_to='pieces_jointes_evaluation_fournisseur/')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_fournisseur_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evaluation_fournisseur_updated', to=settings.AUTH_USER_MODEL)),
                ('fournisseur', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fournisseur.fournisseur')),
                ('type_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fournisseur.typeproduit')),
            ],
        ),
    ]
