# Generated by Django 3.1.3 on 2021-06-27 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SportsBuddyApp', '0008_event_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='confirmed_users',
            field=models.ManyToManyField(blank=True, related_name='events_confirmed_in', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='interested_users',
            field=models.ManyToManyField(blank=True, related_name='events_interested_in', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='SportsBuddyApp.sport'),
        ),
    ]
