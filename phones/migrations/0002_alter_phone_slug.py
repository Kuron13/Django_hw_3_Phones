# Generated by Django 5.0.1 on 2024-02-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
