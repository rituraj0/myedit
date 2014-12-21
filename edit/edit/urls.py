from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import patterns, include, url
from login.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'edit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
    url(r'^create/$', create_new),
    url(r'^edit/', include('login.urls')),
    url(r'^changelist/(?P<file_name>[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})', changelist),
)
