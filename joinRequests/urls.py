from django.urls import path
from .views import send_join_request, accept_join_request

urlpatterns = [
    path('send_join_request/<int:eventID>',
         send_join_request, name='send_join_request'),
    path('accept_join_request/<int:requestID>',
         accept_join_request, name='accept_join_request'),
]
