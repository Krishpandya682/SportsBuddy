from django.shortcuts import get_object_or_404, render
from SportsBuddyApp.models import Sport, Event
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 

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
        #print(**kwargs)
        context['sport_id'] = self.kwargs['sport_id']
        return context

class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

