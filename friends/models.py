from django.db import models
from django.contrib.auth.models import User
from SportsBuddyApp.models import Event
from django.db.models.deletion import CASCADE

# Create your models here.
class FriendsRequest(models.Model):
    from_user=models.ForeignKey(User,related_name='from_user',on_delete=models.CASCADE)
    to_user=models.ForeignKey(User,related_name='to_user',on_delete=models.CASCADE)