"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    # r - raw string
    # '' start and beggining of regex
    # ^ beggining of the string
    # $ end of the string
    url(r'^$', views.index, name='index'),
]