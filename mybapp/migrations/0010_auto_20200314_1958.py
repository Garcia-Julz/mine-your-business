# Generated by Django 3.0.4 on 2020-03-14 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mybapp', '0009_remove_ticket_miner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rig',
            name='miner',
        ),
        migrations.AddField(
            model_name='rig',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]