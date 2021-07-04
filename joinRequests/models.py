from django.db import models
from django.contrib.auth.models import User
from SportsBuddyApp.models import Event
from django.db.models.deletion import CASCADE

# Create your models here.


class JoinRequest(models.Model):
    from_user = models.ForeignKey(
        User, related_name='JoinRequest_from_user', on_delete=CASCADE)
    to_user = models.ForeignKey(
        User, related_name='JoinRequest_to_user', on_delete=CASCADE)
    event = models.ForeignKey(
        Event, related_name='event_join_request', on_delete=CASCADE)
