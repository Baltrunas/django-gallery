# django-gallery
Sumple gallery for django.

## Required
* sorl.thumbnail
* jQuery

## Install
* Copy gallery to apps
* Add 'apps.gallery', to INSTALLED_APPS
* url(r'^gallery/', include('apps.gallery.urls')),
* ./manage.py syncdb

## Use tags
```
{% load gallery %}
{% gallery 1 ['template.html'] %}
```

## To Do
* New HTML 5 templates
	* items-list.html
	* category-carousel.html
* Preview in admin
* Optimize models
