# Generated by Django 5.0.3 on 2024-06-05 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reunion', '0003_remove_decision_meeting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='decision',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='decision',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='decision',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='decision',
            name='updated_by',
        ),
    ]
