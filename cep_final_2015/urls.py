from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, DetailView
from ttrade.models import Request, Favor
from ttrade import views

from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^requestlist/(?P<tag>.*)$', views.RequestList.as_view(), name='requests_list'),
    #url(r'^request/(?P<pk>\d+)$', DetailView.as_view(model=Request), name='detailr'),
    #url(r'^favor/(?P<pk>\d+)$', DetailView.as_view(model=Favor), name='detaill'),
    url(r'^favorlist/(?P<tag>.*)$', views.FavorList.as_view(), name='favors_list'),
    #url(r'^add/request/$', views.RequestCreate.as_view(), name='request_add'),
    url(r'^add/favor/$', views.FavorCreate.as_view(), name='favor_add'),
    url(r'^request/(?P<pk>\d+)/edit/$', views.RequestUpdate.as_view(),  name='request_update'),
    url(r'^favor/(?P<pk>\d+)/edit/$', views.FavorUpdate.as_view(),  name='favor_update'),
    url(r'^request/(?P<pk>\d+)$', views.RequestDetail.as_view(),  name='detailr'),
    url(r'^favor/(?P<pk>\d+)$', views.FavorDetail.as_view(), name='detailf'),
    url(r'^request/(?P<pk>\d+)/delete/$', views.RequestDelete.as_view(),  name='request_delete'),
    url(r'^favor/(?P<pk>\d+)/delete/$', views.FavorDelete.as_view(),  name='favor_delete'),
    url(r'^add/request/$', views.MyViewR.as_view(), name="request_add"),
    #url(r'^add/favor/$', views.MyViewF.as_view(), name="favor_add"),
    url(r'^user/(?P<pk>\d+)$', views.UserDetail.as_view(), name='userdetail'),
    url(r'^acceptRequest/$', views.accept_request, name='acceptrequest'),
    url(r'^accepted/(?P<pk>\d+)$', views.AcceptedList.as_view(), name="accepted_list"),
    url(r'^posted/(?P<pk>\d+)$', views.PostedList.as_view(), name="posted_list"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^favorlistall', views.FavorListAll.as_view(), name="favorlistall"),
)