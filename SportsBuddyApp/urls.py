from django.urls import path

from . import views
from .views import SportListView, EventListView

urlpatterns = [
    path('', views.index, name='index'),
    path('sportslist', SportListView.as_view(), name='sport-list'),
    path('eventslist', EventListView.as_view(), name='event-list'),
       
]