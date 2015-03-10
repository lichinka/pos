from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover ( )

urlpatterns = patterns ('',
    (r'^companies/', include ('companies.urls')),
    (r'^items/', include ('items.urls')),
    (r'^stock/', include ('stock.urls')),
    (r'^utils/', include ('utils.urls')),
    (r'^accounts/', include ('accounts.urls')),
    (r'^sales/', include ('sales.urls')),
    (r'^admin/', include (admin.site.urls))
)

#
# Static data only available during development
#
if settings.DEBUG:
    urlpatterns += patterns ('',
        (r'^js/(?P<path>.*)$', 'django.views.static.serve', 
                               {'document_root': settings.PROJECT_ROOT + '/js/'}),
        (r'^css/(?P<path>.*)$', 'django.views.static.serve', 
                                {'document_root': settings.PROJECT_ROOT + '/css/'}),
        (r'^images/(?P<path>.*)$', 'django.views.static.serve', 
                                {'document_root': settings.PROJECT_ROOT + '/images/'}),
        (r'^media/admin/(?P<path>.*)$', 'django.views.static.serve', 
                                {'document_root': settings.PROJECT_ROOT + '/media/admin/'})
    )
