# Generated by Django 5.0.1 on 2024-02-04 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_rename_content_casestudy_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CaseStudy',
        ),
    ]