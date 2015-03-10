from django.conf.urls.defaults import *

#
# Handles the views for the Items application
#
urlpatterns = patterns ('items.views',
    (r'^$', 'item_list'),
    (r'^categories/$', 'category_list'),
    (r'^items/detail/(?P<item_id>.*)$', 'item_detail'),
    (r'^sizes/$', 'size_group_list'),
    (r'^sizes/detail/(?P<size_group_id>.*)$', 'size_group_detail'),
    (r'^taxes/$', 'tax_list')
)
