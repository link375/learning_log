""" Defines URL patterns for users """

# import path to map to urls
from django.urls import path

# import login view Django 2.0
from django.contrib.auth.views import login

from . import views

app_name = 'users'
urlpatterns = [
    # login page
    # skip the views and render the default django login page
    # use the template from the defined path
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
]