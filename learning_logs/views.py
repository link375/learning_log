from django.shortcuts import render

# import http redirect to re-route to desired page
from django.http import HttpResponseRedirect

# import revers to allow sending users to another url
from django.urls import reverse

# import the model for the date we need
from .models import Topic, Entry

# import the Form
from .forms import TopicForm, EntryForm


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
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic"""
    # get a single topic, based on the topic_id in the url
    topic = Topic.objects.get(id=topic_id)
    # get the entries for this topic based on the date they were added
    # -date_added means sort in descending order
    # Entry is the object
    # use lowercase to set here
    entries = topic.entry_set.order_by('-date_added')
    # context for the template to handle the data
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add a new topic."""

    # how to handle the form submission
    # on page load it will use a GET request so
    # render an empty form
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data
        # on form submission we use POST so do this
        form = TopicForm(request.POST)
        if form.is_valid():  # automatic sanitation vs db <3 python
            form.save()
            # after a successful save go back to the topics page
            # reverse() gets the url
            # then we redirect to that url
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    # render the page and allow form to be monitored
    # when the form is submitted it will use a POST request to the same page
    # so the form should be saved if it's valid
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """add a new entry"""

    # get the topic by using the id from the url
    topic = Topic.objects.get(id=topic_id)

    # check if it's a POST request
    if request.method != 'POST':
        form = EntryForm()
    else:
        # pass the request and data to the form
        form = EntryForm(request.POST)
        if form.is_valid():  # sanitation
            # save as new entry but not to the db yet
            new_entry = form.save(commit=False)
            # add the new_entry to the correct topic based on it's ID
            new_entry.topic = topic
            # now save to the db
            new_entry.save()  # commit is True
            # return to the topic view
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """
    Monitor the edit_entry form and render the edit_entry/id page

    :param request: request when this view is called
    :param entry_id: entry_id from the URL
    :return: save changes / render page
    """

    # get the entry by id from the URI
    entry = Entry.objects.get(id=entry_id)
    # get the topic from the entry object properties
    topic = entry.topic

    # on page load (GET)
    if request != 'POST':
        # fill the form with the current entry
        # this way we can edit it!
        form = EntryForm(instance=entry)
    else:
        # POST data submitted ; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))

    # share tha data with the template
    context = {'entry': entry, 'topic': topic, 'form': form}

    # render the template
    return render(request, 'learning_logs/edit_entry.html', context)

