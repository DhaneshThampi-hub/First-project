# Generated by Django 5.0.3 on 2024-03-22 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_rename_resume_recruiter_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiter',
            name='status',
        ),
    ]
