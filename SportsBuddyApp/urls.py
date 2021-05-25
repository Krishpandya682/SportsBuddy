from django.urls import path

from . import views
from .views import SportListView, EventListView, EventDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('sportslist', SportListView.as_view(), name='sport-list'),
    path('eventslist/<int:sport_id>', EventListView.as_view(), name='event-list'),
    path('eventsdetail/<int:pk>', EventDetailView.as_view(), name='event-detail'),

]