from django.contrib.auth.models import User
from django.urls import path, include

from . import views
from .views import send_friend_request,accept_friend_request

urlpatterns = [
    path('send_friend_request/<int:to_user>',send_friend_request,name='send_friend_request'),
    path('accept_friend_request/<int:requestID>',accept_friend_request,name='accept_friend_request')

]