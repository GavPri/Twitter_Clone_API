# Generated by Django 3.2.23 on 2023-11-08 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='replies',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
