from django.conf.urls import patterns, include, url
# from polls import views
from django.contrib import admin
# from django.contrib.auth import User

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),)
    # url(r'^accounts/profile/(?P<user_id>\d+)', views.profile, name = 'profile'),)