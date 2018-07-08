from django.db import models

# Create your models here.

# each class is the same as a table in the database
# each variable within a class is a column and it's data type
# each __str__ method is what is displayed in the admin panel
# models reference: https://docs.djangoproject.com/en/1.8/ref/models/fields/
class Topic(models.Model):
    """A topic the user is learning about"""
    # max length of a topic name is 200
    text = models.CharField(max_length=200)
    # add the current date
    date_added = models.DateField(auto_now_add=True)

    # this will be displayed in the admin panel
    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    # ForeignKey(other_model, options)
    # connects this to another model by using the same id
    # connects many entries to one topic
    # if the topic is deleted then all entries will be deleted as well
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # no limit on text input here - write as much as you want
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    # this makes entries the plural form rather than entrys
    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        """Return a string representation of the model."""
        # if the entry is longer than 50 chars
        # return the first 50 chars
        # otherwise return the whole entry
        # one char per index
        if int(len(self.text)) >= 50:
            return self.text[:50] + "..."
        else:
            return self.text[:]
