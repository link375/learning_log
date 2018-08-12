# Credits to Eric Matthes

Book: Python Crash Course
Purchase it here: https://amzn.to/2NnR8kT

# learning_log

Start Django app

> django-admin.py startproject <projectName> .

Creating a database

> python manage.py migrate

Run the server

> python manage.py runserver <port>

Start new application

> python manage.py startapp <appname>

Admin page

> http://127.0.0.1:8000/admin/

modifying the database after adding models

> python manage.py makemigrations <appName>

> python manage.py migrate

Create superuser

> python manage.py createsuperuser

> User:ll_admin

> pass: password!

Import migrations

> python manage.py makemigrations <appName>

then run the migrations script again

# Register your models here.

admin.site.register(ModelClass)

# Django Shell

https://docs.djangoproject.com/en/1.8/topics/db/queries/

> python manage.py shell

To show a table in the admin panel

> from django.contrib import admin

> from learning_logs.models import Class, Class2

Show topics

> from learning_logs.models import Topic

> Topic.objects.all()

Example

> topics = Topic.objects.all()

> for topic in topics:

>   print(topic.id, topic)

prints...
1 Chess

2 Rock Climbing

Example 2

> t = Topic.objects.get(id=1)

> t.text

'Chess'

> t.date_added

datetime.datetime(2015, 5, 28, 4, 39, 11, 989446, tzinfo=<UTC>)

or

t.entry_set.all()

# TEMPLATES 

https://docs.djangoproject.com/en/1.8/ref/templates/


# HEROKU 

use gunicorn server locally before live deploy

> heroku local

Deploy to Heroku

> heroku login

> heroku create

> git push heroku master

> heroku ps

> heroku open

Migrate database

> heroku run python manage.py makemigrations

> heroku run python manage.py migrate

Create superuser

> heroku run bash

> python manage.py createsuperuser

> exit

Rename Heroku app

> heroku apps:rename <name>

Destroy project on Heroku

heroku apps:destroy --app <appname>