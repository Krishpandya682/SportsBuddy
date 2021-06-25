from django.contrib.auth.models import User
from django.urls import path, include

from . import views
from .views import UserprofileCreate, profile_view, UserProfileUpdateView

urlpatterns = [
    path('register/', views.register, name='Register'),
    path('', include("django.contrib.auth.urls")),  # <-- added
    path('createProfile/', UserprofileCreate.as_view(),
         name='Create User Profile'),
    path('<pk>/update/', UserProfileUpdateView.as_view()),
    path('viewProfile/', profile_view, name='View User Profile'),

]
