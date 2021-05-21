from django.shortcuts import render
from SportsBuddyApp.models import Sport, Event
from django.http import HttpResponse
from django.views.generic.list import ListView

def index(request):
     return render(request, 'SportsBuddyApp/index.html', {})

class SportListView(ListView):
    model = Sport

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EventListView(ListView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
