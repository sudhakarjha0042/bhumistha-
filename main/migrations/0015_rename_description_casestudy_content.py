# Generated by Django 5.0.1 on 2024-02-04 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_casestudy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casestudy',
            old_name='description',
            new_name='content',
        ),
    ]
