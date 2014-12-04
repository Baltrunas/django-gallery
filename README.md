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
{% gallery 1 %}
```

## To Do
* New templates
* Optimization
* Custom template for templatetags
* recreate thumb
* default from settings
* image filter
* HTML 5
* Preview
* Если высота больше ширины, обрезать по верху
