# Generated by Django 3.0.5 on 2020-04-18 20:48

import candidate.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_professional_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='upload',
            field=models.FileField(upload_to=candidate.models.user_directory_path, verbose_name='Файл'),
        ),
    ]
