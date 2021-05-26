from django import forms
from SportsBuddyApp.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['location', 'sport', 'start_time',
                  'end_time', 'radius', 'proficiency', 'competitive']
