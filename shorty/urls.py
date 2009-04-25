from django.conf.urls.defaults import *
from views import make, list, redirect
urlpatterns = patterns('',
    url(r'^list/$', list, name='url-list'),
    url(r'^make/$', make, name='make-new'),
    url(r'^(?P<key>[a-zA-Z0-9]{1,10})$', redirect, name='redirect-to'),
    
)
