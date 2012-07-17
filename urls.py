# -*- coding: utf-8 -*
from django.conf.urls import patterns, include, url

urlpatterns = patterns('gallery.views',
    url(r'^$', 'category_list', name='gallery_category_list'),
    url(r'^(?P<url>[-\w/\_]+)/$', 'category_detail', name='gallery_category'),
)