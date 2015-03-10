from django.conf.urls.defaults import *

#
# Handles the views for the Stock application
#
urlpatterns = patterns ('sales.views',
    (r'^$', 'open_sale_list'),
    (r'^open_sale_list/$', 'open_sale_list'),
    (r'^closed_sale_list/$', 'closed_sale_list'),
    (r'^detail/(?P<sale_id>.*)$', 'sale_detail_list'),
)
