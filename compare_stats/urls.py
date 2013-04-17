#!/usr/bin/env python

from django.conf.urls.defaults import patterns, url

from compare_stats import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='compare_stats_home'),
    # url(r'^states.json/$'),
    # url(r'^search/$', views.search),
    )