from registration.models import UserProfile
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from SportsBuddyApp.models import Sport, Event
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from login_required import login_not_required

from .forms import EventForm


@login_not_required
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'SportsBuddyApp/index.html', {"user_id": request.user})


def create_event_view(request):
    context = {}

    # create object of form
    form = EventForm(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():
        print("database change")

        sport = form.cleaned_data['sport']
        temp_form = form.save(commit=False)
        temp_form.creator = request.user
        print("User change")

        temp_form.save()

        user_profile = UserProfile.objects.get(user=request.user)
        print(user_profile)
        user_profile.created_events.add(form.instance)
        user_profile.save()
        sport.increment_event()
        sport.save()

        return redirect("/home")
        # save the form data to model
        # form.save()

    context['form'] = form
    return render(request, "SportsBuddyApp/create_event.html", context)


def join_event_view(request, event_id):
    event = Event.objects.filter(pk=event_id)[0]
    event.interested_users.add(request.user)
    return render(request, 'SportsBuddyApp/join_event.html', {})


def joined_events_list(request):
    joinedEventsList = []
    for event in Event.objects.all():
        if not event.creator is request.user:
            if request.user in event.interested_users.all():
                joinedEventsList.append(event)
    return render(request, 'SportsBuddyApp/joined_events_list.html', {"joined_events_list": joinedEventsList})


def my_events_view(request):
    myEventsList = Event.objects.all()
    return render(request, 'SportsBuddyApp/my_events.html', {"my_events_list": myEventsList})


class SportListView(ListView):
    model = Sport

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EventListView(ListView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(**kwargs)
        context['sport_id'] = self.kwargs['sport_id']
        return context


class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
