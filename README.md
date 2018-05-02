# learning_log
Simple Django App

- Run the server

python manage.py runserver

- Admin page

http://127.0.0.1:8000/admin/

- modifying the database after adding models
python manage.py makemigrations learning_logs
python manage.py migrate

- create superuser

python manage.py createsuperuser
User:ll_admin
pass: password!

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