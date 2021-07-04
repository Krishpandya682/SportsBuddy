from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import response
from registration.models import UserProfile
from notifications.models import Notification, Types
from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404
from django import http
from .models import FriendsRequest
from django.http import HttpResponse
from registration.models import UserProfile
# Create your views here.


@login_required
def send_friend_request(request, to_user):
    from_user = request.user
    to_user = User.objects.get(id=to_user)

    friend_request, created = FriendsRequest.objects.get_or_create(
        from_user=from_user, to_user=to_user)
    notifications = Notification.objects.create(
        user=to_user, type=Types.FRND_RQST_RECIEVED, frndRqst=friend_request)

    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend rewuest not sent')


@login_required
def accept_friend_request(request, requestID):

    friend_request = FriendsRequest.objects.get(id=requestID)
    to_profile = friend_request.to_user.userprofile
    from_profile = friend_request.from_user.userprofile
    if friend_request.to_user == request.user:
        to_profile.friends_list.add(friend_request.from_user)
        from_profile.friends_list.add(friend_request.to_user)
        friend_request.delete()
        notifications = Notification.objects.create(
            user=friend_request.from_user, type=Types.FRND_RQST_ACCEPTED, frndRqst=friend_request)

        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('not accepted')


@login_required
def view_Profile(request, user_id):
    user = User.objects.get(id=user_id)
    print(user)
    user_profile = user.userprofile
    return render(request, "friends/user_view_profile.html", {'userprofile': user_profile})
