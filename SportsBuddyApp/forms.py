from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from SportsBuddyApp.models import Event

from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class EventForm(forms.ModelForm):
    start = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'timepicker'}))
    start_time = forms.TimeField(widget=TimePickerInput(format='%I:%M %p'))

    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'sport', 'start_time', 'start_date',
                  'end_time', 'radius', 'proficiency', 'num_of_players', 'competitive']
        widgets = {
            'start_date': DateInput(),
            'start_time': DateTimePickerInput(
                options={
                    'minDate': (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00'),
                    'maxDate': (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d 23:59:59'),
                    'enabledHours': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                }
            ),
            'end_time': DateTimePickerInput()
        }
