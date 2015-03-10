from django.conf.urls.defaults import *

#
# Handles the views for the Companies application
#
urlpatterns = patterns ('companies.views',
    (r'^$', 'index'), 
    (r'^(?P<company_id>\d+)/$', 'detail')
)
