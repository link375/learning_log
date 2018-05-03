from django.db import models

# Create your models here.

# each class is the same as a table in the database
# each variable within a class is a column and it's data type
# each __str__ method is what is displayed in the admin panel
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    # this makes entries the plural form rather than entrys
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if int(len(self.text)) >= 50:
            return self.text[:50] + "..."
        else:
            return self.text[:]
