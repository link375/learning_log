from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register(request):
    """
    register a new user
    :param request: GET or POST request
    :return: GET - empty form
            POST - process the form
    """
    if request.method != 'POST':
        # display blank registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)

        # if the form is valid (no bad input
        #  then save it to new_user
        if form.is_valid():
            new_user = form.save()
            # log the user in and then redirect to home page
            # since the user has been saved we can use the new
            # username attribute
            # we use the password from the forms POST request
            # there are 2 passwords and they matched because
            # the form was valid so use password1 or password2
            # if the user and pass is valid it will return true
            # and get stored in authenticated_user
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            # now we login the user using the credentials above
            login(request, authenticated_user)
            # now we send the user to the home page
            return HttpResponseRedirect(reverse('learning_logs:index'))

    # if it's a GET request then render the register.html page
    context = {'form': form}
    return render(request, 'users/register.html', context)
