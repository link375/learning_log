# Credits to Eric Matthes

Book: Python Crash Course
Purchase it here: https://amzn.to/2NnR8kT

# learning_log


Simple Django App

Start Django app

django-admin.py startproject <projectName> .

creating a database

python manage.py migrate

- Run the server

python manage.py runserver <port>

- start new application

python manage.py startapp <appname>

- Admin page

http://127.0.0.1:8000/admin/

- modifying the database after adding models
python manage.py makemigrations <appName>
python manage.py migrate

- create superuser

python manage.py createsuperuser
User:ll_admin
pass: password!

- import migrations

python manage.py makemigrations <appName>

-then run the migrations script again

To show a table in the admin panel

from django.contrib import admin

from learning_logs.models import Class, Class2

# Register your models here.

admin.site.register(ModelClass)
admin.site.register(ModelClass)

- Django Shell

python manage.py shell

from learning_logs.models import Topic

Topic.objects.all()

- example

topics = Topic.objects.all()

for topic in topics:

print(topic.id, topic)

prints...
1 Chess

2 Rock Climbing

- example 2

t = Topic.objects.get(id=1)

t.text

'Chess'

t.date_added

datetime.datetime(2015, 5, 28, 4, 39, 11, 989446, tzinfo=<UTC>)

or

t.entry_set.all()

querying data
https://docs.djangoproject.com/en/1.8/topics/db/queries/

TEMPLATE 

https://docs.djangoproject.com/en/1.8/ref/templates/