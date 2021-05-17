from django.urls import path, include

from . import views

urlpatterns = [
    path('register', views.register, name='Register'),
    path('', include("django.contrib.auth.urls")), # <-- added
]