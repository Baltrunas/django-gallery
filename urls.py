# -*- coding: utf-8 -*
from django.conf.urls import patterns, include, url

urlpatterns = patterns('gallery.views',
    url(r'^(?P<full_url>[-\w]+)/$', 'category_detail', name='category_detail'),
)