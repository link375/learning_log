from django.shortcuts import render

# import the model for the date we need
from .models import Topic

# Create your views here.

def index(request):
    """The home page for Learning Log"""
    # return an html template
    # path is relative from the location of views.py/templates
    # assumes it's in a templates directory
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics"""
    # query the database for topics by date added
    topics = Topic.objects.order_by('date_added')
    # context is a
    # dictionary in which the keys are names
    # context that will be sent to the template
    # keys - names used in the template to display data
    # value - data in each topic
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic"""
    # get a single topic, based on the topic_id in the url
    topic = Topic.objects.get(id=topic_id)
    # get the entries for this topic based on the date they were added
    # -date_added means sort in descending order
    entries = topic.entry_set.order_by('-date_added')
    # context for the template to handle the data
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
