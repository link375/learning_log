from django.contrib import admin

# import classes (models) here to register with the admin
from learning_logs.models import Topic, Entry

# users and groups are automatically available
# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)

