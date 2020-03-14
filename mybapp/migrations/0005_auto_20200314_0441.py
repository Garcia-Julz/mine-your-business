# Generated by Django 3.0.4 on 2020-03-14 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybapp', '0004_auto_20200314_0325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issuetype',
            options={'verbose_name': 'itn', 'verbose_name_plural': 'itns'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'city', 'verbose_name_plural': 'cities'},
        ),
        migrations.RenameField(
            model_name='issuetype',
            old_name='issue',
            new_name='itn',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='issue_type_name',
            new_name='itn',
        ),
    ]
