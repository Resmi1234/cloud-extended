# Generated by Django 4.0.2 on 2022-03-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extendedcloudapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='Files',
            field=models.FileField(unique=True, upload_to=''),
        ),
    ]
