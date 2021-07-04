from django.urls import path

from . import views
from .views import SportListView, EventListView, EventDetailView, create_event_view, join_event_view, my_events_view, joined_events_list, UserListView, friends_list_view
#from SportsBuddy.SportsBuddyApp.views import create_event_view

app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
    path('sportslist/', SportListView.as_view(), name='sport-list'),
    path('eventslist/<int:sport_id>', EventListView.as_view(), name='event-list'),
    path('eventsdetail/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    path('eventsdetail/<int:event_id>/join/',
         join_event_view, name='join-event'),
    path('joinedevents/', joined_events_list, name='joined_events'),
    path('createevent/', create_event_view, name='create_event'),
    path('myevents/', my_events_view, name='my_events'),
    path('findfriends/', UserListView.as_view(), name='user-list'),
    path('friendslist/', friends_list_view, name='friends_list'),

]
