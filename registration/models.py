from django.db import models
from django.contrib.auth.models import User
from SportsBuddyApp.models import Event
from django.db.models.deletion import CASCADE
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, blank=False)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True)
    friends_list = models.ManyToManyField(
        User, related_name='friends_list', blank=True)

    def __str__(self):
        return self.user.username
