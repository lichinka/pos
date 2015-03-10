from django.conf.urls.defaults import *

#
# Handles the views for the Items application
#
urlpatterns = patterns ('utils.views',
    (r'^$', 'index')
)
