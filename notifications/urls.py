from django.contrib.auth.models import User
from django.urls import path, include

from .views import notification_list_view

urlpatterns = [
    path('', notification_list_view, name='Notifications'),

]
