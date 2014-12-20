from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import patterns, include, url
from login.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'edit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<file_name>[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})/$', edit_code),                    
)
