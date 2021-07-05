from notifications.models import Notification
import notifications
from django.shortcuts import render
from .models import Types
# Create your views here.


def notification_list_view(request):
    notification = Notification.objects.all()[0]
    print(notification.type)
    if notification.type == "Join Request Recieved":
        print("yes")
    return render(request, 'notifications/notification_list.html')
