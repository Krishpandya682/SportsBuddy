from django.urls import path, include

from . import views
from .views import create_user_profile_view, profile_view

urlpatterns = [
    path('register', views.register, name='Register'),
    path('', include("django.contrib.auth.urls")),  # <-- added
    path('createProfile', create_user_profile_view, name='Create User Profile'),
    path('viewProfile', profile_view, name='View User Profile'),

]
