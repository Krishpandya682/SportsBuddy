from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from SportsBuddyApp.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['event_name', 'sport', 'start_time',
                  'end_time', 'radius', 'proficiency', 'num_of_players', 'competitive']
