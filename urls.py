from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.category_list, name='gallery_category_list'),
	url(r'^(?P<url>[-\w/\_]+)/(?P<id>[\d]+)/$', views.item_detail, name='gallery_item_detail'),
	url(r'^(?P<url>[-\w/\_]+)/$', views.category_detail, name='gallery_category_detail'),
]
