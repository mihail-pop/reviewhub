# Generated by Django 4.1.13 on 2024-05-20 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proiect', '0010_conference_trackers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadeddocument',
            old_name='workplace',
            new_name='keywords',
        ),
    ]
