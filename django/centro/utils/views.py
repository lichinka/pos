from django import forms
from django.conf import settings
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from companies.models import Terminal



def render (template, data, context):
    """
    A wrapper around the Django function 'render_to_response' to
    include data used in all our templates.
    """
    data['terminal_name'] = Terminal.objects.get (pk=settings.THIS_TERMINAL_ID)
    data['application_name'] = settings.APPLICATION_NAME
    data['application_version'] = settings.APPLICATION_VERSION

    return render_to_response (template, data, context)


def render_login (request):
    """
    A wrapper around the Django login view to
    include data used in our template.
    """
    data = dict ( )
    data['terminal_name'] = Terminal.objects.get (pk=settings.THIS_TERMINAL_ID)
    data['application_name'] = settings.APPLICATION_NAME
    data['application_version'] = settings.APPLICATION_VERSION

    #
    # Display only active users that may login into this terminal
    #
    this_terminal = Terminal.objects.get (pk=settings.THIS_TERMINAL_ID)
    all_users = User.objects.filter (userprofile__terminals__in = [this_terminal]).\
                             filter (is_active = '1')
    #
    # Divide the users in groups of three each
    # to make it easier to render the login page
    #
    data['user_groups'] = list ( )

    for i in range (0, len(all_users), 3):
        data['user_groups'].append (all_users[i:i+3])

    return views.login (request, extra_context=data)


def index (request):
    """
    FIXME: a view to import data from CSV files.
    """
    class UploadFileForm (forms.Form):
        """
        A form to upload the CSV file.
        """
        title = forms.CharField (max_length=50)
        upfile = forms.FileField ( )

    if (request.method == 'POST'):
        form = UploadFileForm (request.POST, request.FILES)
        if (form.is_valid ( )):
            handle_uploaded_file (request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm ( )

    return render_to_response ('utils/index.html', 
                               {'form': form},
                               context_instance = RequestContext (request))

