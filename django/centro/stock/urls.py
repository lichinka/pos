from django.conf.urls.defaults import *

#
# Handles the views for the Stock application
#
urlpatterns = patterns ('stock.views',
    (r'^$', 'index')
)
