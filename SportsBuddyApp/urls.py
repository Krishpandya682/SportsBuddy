from django.urls import path

from . import views
from .views import SportListView, EventListView, EventDetailView,create_event_view
#from SportsBuddy.SportsBuddyApp.views import create_event_view

urlpatterns = [
    path('', views.index, name='index'),
    path('sportslist', SportListView.as_view(), name='sport-list'),
    path('eventslist/<int:sport_id>', EventListView.as_view(), name='event-list'),
    path('eventsdetail/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    path('createevent',create_event_view,name='create_event')
]