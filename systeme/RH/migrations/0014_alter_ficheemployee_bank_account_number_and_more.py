# Generated by Django 5.0.3 on 2024-04-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0013_alter_employe_email_alter_ficheemployee_work_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficheemployee',
            name='bank_account_number',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='ficheemployee',
            name='cin',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='ficheemployee',
            name='cnss',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='ficheemployee',
            name='work_mobile',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='ficheemployee',
            name='work_phone',
            field=models.CharField(max_length=8),
        ),
    ]
