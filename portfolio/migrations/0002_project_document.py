# Generated by Django 3.0.6 on 2020-05-27 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='document',
            field=models.FileField(blank=True, upload_to='portfolio/documents/'),
        ),
    ]
