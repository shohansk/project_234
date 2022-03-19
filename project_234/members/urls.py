import tempfile
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import UserEditView , UserRegisterView,PasswordsChangeView

urlpatterns = [
    
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    path('password/',PasswordsChangeView.as_view()),

]