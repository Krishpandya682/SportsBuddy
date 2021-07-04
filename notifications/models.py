from django.db import models
from django.contrib.auth.models import User
from friends.models import FriendsRequest
from joinRequests.models import JoinRequest
from django.db.models.deletion import CASCADE
# Create your models here.


class Types(models.TextChoices):
    NONE = 'None'
    FRND_RQST_RECIEVED = 'Friend Request Recieved'
    JOIN_RQST_RECIEVED = 'Join Request Recieved'
    FRND_RQST_ACCEPTED = 'Friend Request Accepted'
    JOIN_RQST_ACCEPTED = 'Join Request Accepted'


class Notification(models.Model):
    user = models.OneToOneField(
        User, related_name='notification_user', on_delete=CASCADE, blank=False)
    type = models.IntegerField(
        default=Types.NONE, choices=Types.choices)
    frndRqst = models.ForeignKey(
        FriendsRequest, related_name='notification_frnd_rqst', on_delete=CASCADE, blank=True)
    joinRqst = models.ForeignKey(
        JoinRequest, related_name='notification_join_rqst', on_delete=CASCADE, blank=True)
