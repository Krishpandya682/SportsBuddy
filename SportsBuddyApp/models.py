from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Proficiency(models.IntegerChoices):
    LOW = '0'
    MEDIUM= '1'
    HIGH = '2'

class Sport(models.Model):
    name = models.CharField(max_length=50)
    open_events = models.IntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    sport = models.ForeignKey(Sport, on_delete=CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    radius =models.IntegerField()
    proficiency = models.IntegerField(default= Proficiency.LOW, choices=Proficiency.choices)
    competitive = models.BooleanField(default = False)
    #rating = models.IntegerField()

    def __str__(self):
        return self.user.username


        
