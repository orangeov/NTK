# Generated by Django 3.0.5 on 2020-04-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0003_auto_20200419_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='program',
            field=models.CharField(max_length=60, verbose_name='Специальность'),
        ),
    ]