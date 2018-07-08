"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# import admin since it has its own url
from django.contrib import admin
# import path and include to allow us to map
# urls from other apps
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # add the url to the learning_logs app
    # you can also use a 3rd argument to specify
    # a namespace namespace='learning_logs'
    # this will avoid confusing it with another apps urls.py
    path('', include('learning_logs.urls'), name='learning_logs'),
]