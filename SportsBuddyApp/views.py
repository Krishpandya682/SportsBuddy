from django.shortcuts import get_object_or_404, render,redirect
from SportsBuddyApp.models import Sport, Event
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.contrib.auth.decorators import login_required

from .forms import EventForm

def index(request):
    if  not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'SportsBuddyApp/index.html', {"user_id":request.user})

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

@login_required 
def create_event_view(request):
    context ={}
  
    # create object of form
    form = EventForm(request.POST or None, request.FILES or None)
    print("Function Accessed")
    # check if form data is valid
    if form.is_valid():
        print("Form is Valid")
        temp_form=form.save(commit=False)
        temp_form.user=request.user
        temp_form.save()
        return HttpResponse('Hurray, saved!')
        # save the form data to model
        #form.save()
  
    context['form']= form
    return render(request, "SportsBuddyApp/create_event.html", context)