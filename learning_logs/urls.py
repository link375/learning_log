"""Defines url patterns for learning_logs."""

# import path to allow use to use path mapping
from django.urls import path

# import the view - or templates
from . import views

# define the name for this app
# we can use this as a namespace
app_name = 'learning_logs'

# urls that should come to this app
urlpatterns = [
    # Home page.
    # url/pattern/URI, templateLocation, nameOfURL
    path('', views.index, name='index'),

    # Show all topics
    # show single topics if its ID is specified
    path('topics/', views.topics, name='topics'),

    # Show individual topic
    # <int:topic_id> will store whatever is there as an int
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing entries
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),


    # add new urls
]