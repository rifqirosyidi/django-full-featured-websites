# Generated by Django 2.2.4 on 2019-08-12 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='images',
            new_name='image',
        ),
    ]
