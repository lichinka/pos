from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _
from utils.views import render_login


def index (request):
    """
    The default view.
    """
    pass


def log_user_in (request):
    """
    The login view to authenticate users.
    """
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['geslo']
        user = authenticate (username=username, 
                             password=password)
        if (user is not None):
            if (user.is_active):
                #
                # Log the user in
                #
                login (request, user)

                #
                # If the user has access to the admin page, redirect
                #
                if (user.is_staff):
                    return redirect (settings.ADMIN_URL)
                else:
                    return redirect (settings.LOGIN_REDIRECT_URL)
            else:
                #
                # Return a 'disabled account' error message
                #
                return HttpResponse (_('Your account has been disabled'))

    return render_login (request)

