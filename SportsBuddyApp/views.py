from registration.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from SportsBuddyApp.models import Sport, Event
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from login_required import login_not_required
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db.models import Q
from .forms import EventForm


@login_not_required
def index(request):
    context = {}
    if request.user.is_authenticated:
        context = {"user": request.user}
    return render(request, 'SportsBuddyApp/index.html', context)


def create_event_view(request):
    context = {}
    # create object of form
    form = EventForm(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():

        sport = form.cleaned_data['sport']
        temp_form = form.save(commit=False)
        temp_form.creator = request.user

        temp_form.save()

        user_profile = request.user.userprofile
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
    user_profile = request.user.userprofile
    print(user_profile)
    user_profile.joined_events.add(event)
    user_profile.save()
    return render(request, 'SportsBuddyApp/join_event.html', {})


def joined_events_list(request):
    user_profile = request.user.userprofile
    return render(request, 'SportsBuddyApp/joined_events_list.html', {'userprofile': user_profile})


def my_events_view(request):
   # user_profile = request.user.userprofile
    # , {'userprofile': user_profile})
    print(request.user.events.all())
    return render(request, 'SportsBuddyApp/my_events.html')


class SportListView(ListView):
    model = Sport
    template_name = 'SportsBuddyApp/sport_list.html'

    def get(self, request):

        strval = request.GET.get("search", False)
        print(strval)
        if strval:
            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(name__icontains=strval)
            sport_list = Sport.objects.filter(
                query).select_related().distinct().order_by('open_events')[:10]
        else:
            sport_list = Sport.objects.all().order_by('open_events')[:10]

        ctx = {'sport_list': sport_list, 'search': strval}
        return render(request, self.template_name, ctx)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EventListView(ListView):
    model = Event
    template_name = 'SportsBuddyApp/event_list.html'

    def get(self, request, sport_id):

        sport = Sport.objects.get(id=self.kwargs['sport_id'])
        event_list = sport.events.all()
        strval = request.GET.get("search", False)
        print(strval)
        if strval:
            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(event_name__icontains=strval)
            query.add(Q(event_description__icontains=strval), Q.OR)
            event_list = event_list.filter(
                query).select_related().distinct().order_by('event_name')[:10]
        else:
            event_list = event_list.order_by('event_name')[:10]
        print(event_list)
        ctx = {'event_list': event_list,
               'search': strval, 'sport_id': sport_id}
        return render(request, self.template_name, ctx)

    def get_context_data(self, **kwargs):
        sport = Sport.objects.get(id=self.kwargs['sport_id'])
        context = super().get_context_data(**kwargs)
        # print(**kwargs)
        context['sport_id'] = self.kwargs['sport_id']
        context['sport'] = sport
        return context


class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SportListView(ListView):
    model = Sport
    template_name = 'SportsBuddyApp/sport_list.html'

    def get(self, request):

        strval = request.GET.get("search", False)
        print(strval)
        if strval:
            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(name__icontains=strval)
            sport_list = Sport.objects.filter(
                query).select_related().distinct().order_by('open_events')[:10]
        else:
            sport_list = Sport.objects.all().order_by('open_events')[:10]

        ctx = {'sport_list': sport_list, 'search': strval}
        return render(request, self.template_name, ctx)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserListView(ListView):
    model = User
    template_name = 'SportsBuddyApp/user_list.html'

    def get(self, request):

        strval = request.GET.get("search", False)
        print(strval)
        if strval:
            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(username__icontains=strval)
            user_list = User.objects.filter(
                query).select_related().distinct().order_by('username')[:10]
        else:
            user_list = User.objects.all().order_by('username')[:10]

        ctx = {'user_list': user_list, 'search': strval}
        return render(request, self.template_name, ctx)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
