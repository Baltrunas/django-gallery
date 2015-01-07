from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.gallery, name='gallery'),
	url(r'^(?P<url>[-\w/\_]+)/$', views.category, name='gallery_category'),
]
