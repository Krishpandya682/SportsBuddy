# from django.shortcuts import render

# from django.http import HttpResponse


# def register(request):
#      return render(request, 'registration/register.html', {})

# views.py
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.http import response
from registration.models import UserProfile
from django.shortcuts import render, redirect
from .forms import RegisterForm, UserProfileForm
from login_required import login_not_required
from django import http

# Create your views here.


@login_not_required
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/createUser/createProfile")
    else:

        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})


class UserprofileCreate(CreateView):

    # specify the model for create view
    model = UserProfile

    # specify the fields to be displayed
    fields = ['profile_pic', 'bio']
    def form_valid(self, form):
        user_profile = form.save(commit=False)
        user_profile.user_id = self.request.user.id
        user_profile.save()
        return redirect('/createUser/viewProfile')


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    
    fields = ['profile_pic', 'bio']

    success_url = "/createUser/viewProfile"


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "registration/view_profile.html", {"userprofile": UserProfile.objects.get(user=request.user)})
