# -*- coding: utf-8 -*
from django.conf.urls import patterns
# from django.conf.urls import include
from django.conf.urls import url

urlpatterns = patterns('gallery.views',
	url(r'^$', 'category_list', name='gallery_category_list'),
	url(r'^item/(?P<id>[\d]+)/$', 'item_detail', name='item_detail'),
	url(r'^(?P<url>[-\w/\_]+)/(?P<id>[\d]+)/$', 'item_detail', name='item_detail'),
	url(r'^(?P<url>[-\w/\_]+)/$', 'category_detail', name='gallery_category'),
)
