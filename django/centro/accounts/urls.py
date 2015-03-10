from django.conf.urls.defaults import *


#
# Handles the views for the Accounts application
#
urlpatterns = patterns ('accounts.views',
    (r'^$', 'index'),
    (r'^login/$', 'log_user_in')
)
