from django.contrib.auth.models import User
from django.urls import path, include

from . import views
from .views import send_friend_request, accept_friend_request, view_Profile

urlpatterns = [
    path('send_friend_request/<int:eventID>',
         send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:requestID>',
         accept_friend_request, name='accept_friend_request'),
    path('view_profile/<int:user_id>', view_Profile, name='view_profile'),
]
