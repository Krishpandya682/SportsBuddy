# from django.shortcuts import render

# from django.http import HttpResponse


# def register(request):
#      return render(request, 'registration/register.html', {})

# views.py
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.http import response
from registration.models import UserProfile
from django.shortcuts import render, redirect
from .forms import RegisterForm, UserProfileForm
from login_required import login_not_required

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


def create_user_profile_view(request):
    context = {}

    # create object of form
    form = UserProfileForm(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():
        temp_form = form.save(commit=False)
        temp_form.user = request.user
        temp_form.save()
        return redirect("/home")
        # save the form data to model
        # form.save()

    context['form'] = form
    return render(request, "registration/create_profile.html", context)


class ProfileView(DetailView):
    model = UserProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
