# Generated by Django 3.0.8 on 2021-05-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportsBuddyApp', '0002_remove_event_competive'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='competive',
            field=models.BooleanField(default=False),
        ),
    ]