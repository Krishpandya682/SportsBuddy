from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.


class Proficiency(models.IntegerChoices):
    LOW = '0'
    MEDIUM = '1'
    HIGH = '2'


class Sport(models.Model):
    name = models.CharField(max_length=50)
    open_events = models.IntegerField()

    def __str__(self):
        return self.name

    def increment_event(self):
        print("increment function")
        print(self.open_events)
        self.open_events = self.open_events+1
        print(self.open_events)

#Comment
class Event(models.Model):
    event_name = models.CharField(max_length=50, default="Event Name")
    event_description = models.TextField(default="Event Description")
    creator = models.ForeignKey(
        User, on_delete=CASCADE, related_name='events', default=None)
    sport = models.ForeignKey(Sport, related_name='events', on_delete=CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    radius = models.IntegerField()
    num_of_players = models.IntegerField(default=1)
    proficiency = models.IntegerField(
        default=Proficiency.LOW, choices=Proficiency.choices)
    competitive = models.BooleanField(default=False)
    interested_users = models.ManyToManyField(
        User, related_name="events_interested_in", blank=True)
    confirmed_users = models.ManyToManyField(
        User, related_name="events_confirmed_in", blank=True)
    #rating = models.IntegerField()

    def __str__(self):
        return self.event_name
