import joinRequests
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import response
from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404
from django import http
from .models import JoinRequest
from django.http import HttpResponse
from registration.models import UserProfile
from notifications.models import Notification, Types
from SportsBuddyApp.models import Event
# Create your views here.


@login_required
def send_join_request(request, eventID):
    from_user = request.user
    event = Event.objects.get(id=eventID)
    to_user = event.creator

    join_request, created = JoinRequest.objects.get_or_create(
        from_user=from_user, to_user=to_user, event=event)

    if created:
        notifications = Notification.objects.create(
            user=to_user, type=Types.JOIN_RQST_RECIEVED, joinRqst=join_request)

        event.interested_users.add(join_request.from_user)
        return HttpResponse('join request sent')
    else:
        return HttpResponse('join request not sent')


@login_required
def accept_join_request(request, requestID):

    join_request = JoinRequest.objects.get(id=requestID)
    event = join_request.event
    from_user = join_request.from_user
    to_user = join_request.to_user
    join_request.delete()
    if to_user == request.user:
        event.confirmed_users.add(from_user)
        event.interested_users.remove(from_user)
        notifications = Notification.objects.create(
            user=from_user, type=Types.JOIN_RQST_ACCEPTED, frndRqst=None, joinRqst=None)
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('not accepted')
