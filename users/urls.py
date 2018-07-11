""" Defines URL patterns for users """

from django.urls import path
from django.contrib.auth.views import auth_login

from . import views

app_name = 'users'
urlpatterns = [
    # login page
    # skip the views and render the default django login page
    # use the template from the defined path
    path('login/',
         auth_login, {'template_name': 'users/login.html'},
         name='login')
]