"""SportsBuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include
from registration import views as v
from django.conf import settings
from django.conf.urls.static import static


appName = "SportsBuddy"

urlpatterns = [
    path('home/', include('SportsBuddyApp.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('createUser/', include('registration.urls'), name='createUser'),
    path('friends/',include('friends.urls'),name='friends')
    # path("register/", v.register, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
