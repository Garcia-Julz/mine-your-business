# Generated by Django 3.0.4 on 2020-03-13 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='city',
        ),
    ]