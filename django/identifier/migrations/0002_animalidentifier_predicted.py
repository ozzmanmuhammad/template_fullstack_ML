# Generated by Django 4.1.7 on 2023-03-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identifier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalidentifier',
            name='predicted',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
