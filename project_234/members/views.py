from re import template
from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm ,EditProfileForm

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('home')