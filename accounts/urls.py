from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib.auth.views import login, logout
from accounts import views

urlpatterns = patterns('',
    url(r'^login/$', login, {'template_name':'accounts/login.html'},name='login'), 
    url(r'^logout/$', logout, {'next_page':'/'}, name='logout'), 
    url(r'^register/$', 'accounts.views.registration', name='register'),
    url(r'^karmaup/$', views.karma_up, name='karma_up'),
    url(r'^karmadown/$', views.karma_down, name='karma_down'),
    #url(r'^(?P<pk>\d+)/edit/$', views.UserProfileUpdate.as_view(),  name='userprofile_update'),
)