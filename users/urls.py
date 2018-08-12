""" Defines URL patterns for users """

### REMEMBER TO REGISTER THIS APP IN THE SETTINGS ###

# import path to map to urls
from django.urls import path

# import login view Django 2.1
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    # login page
    # skip the views and render the default django login page
    # use the template from the defined path
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),

    # Logout link
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # registration page
    path('register/', views.register, name='register'),


]