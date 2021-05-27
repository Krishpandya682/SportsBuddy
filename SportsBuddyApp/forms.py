from django import forms
from SportsBuddyApp.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['sport', 'start_time',
                  'end_time', 'radius', 'proficiency', 'num_of_players', 'competitive']
