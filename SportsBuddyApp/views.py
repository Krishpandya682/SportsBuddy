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
    context = {"user_id": request.user}
    user_profile = UserProfile.objects.get(user=request.user)

    if request.user.is_authenticated:
        context['userprofile'] = user_profile
    print('****************')
    print(user_profile.profile_pic)
    return render(request, 'SportsBuddyApp/index.html', context)


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

        temp_form.save()

        user_profile = UserProfile.objects.get(user=request.user)
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
    user_profile = UserProfile.objects.get(user=request.user)
    print(user_profile)
    user_profile.joined_events.add(event)
    user_profile.save()
    return render(request, 'SportsBuddyApp/join_event.html', {})


def joined_events_list(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'SportsBuddyApp/joined_events_list.html', {'userprofile': user_profile})


def my_events_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'SportsBuddyApp/my_events.html', {'userprofile': user_profile})


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
