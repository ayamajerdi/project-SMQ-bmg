# Generated by Django 5.0.3 on 2024-06-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reunion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='type_reunion',
            field=models.CharField(choices=[('Team Meeting', 'Team Meeting'), ('Client Meeting', 'Client Meeting'), ('Project Meeting', 'Project Meeting'), ('One-on-One', 'One-on-One'), ('Brainstorming', 'Brainstorming')], default=None, max_length=50),
        ),
    ]
