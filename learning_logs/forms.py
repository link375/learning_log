"""Create forms for user input"""

from django import forms

from .models import Topic

# Create a form to add Topics
# Create an input text field
# Populate the input box with an empty string
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}