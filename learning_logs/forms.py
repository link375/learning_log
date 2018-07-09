"""Create forms for user input"""

from django import forms

from .models import Topic, Entry


# Create a form to add Topics
# Create an input text field
# Populate the input box with an empty string
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


# create a form for the entries
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # css make the width 80 cols; standard: 40
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}