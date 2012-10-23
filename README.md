# django-gallery
Images gallery for django.

# Install
* Add 'gallery', to INSTALLED_APPS
* url(r'^gallery/', include('gallery.urls')),
* ./manage.py syncdb

# Futures
* New templates
* Optimization
* Custom template for templatetags
* README.md
* recreate thumb
* default from settings
* image filter

# Changelog
## 2012.07.19
### Add
* templatetag gallery_catgory id size type ('thumb' or 'original' or 'WIDTHxHEIGHT')

### Fix
* templatetag gallery_image id size type


## 2012.07.17
### Add
* colorbox
* templatetag gallery_image id size ('thumb' or 'original' or 'WIDTHxHEIGHT')

## 2012.07.15
### Add
* Category
* Image
* Category display method.
* Simple settings.

### Fix
* Optimized category get_absolute_url method.
* Optimized category url_puth method.
* Optimized category save method.
* Remove category puth method.

<!-- 	цветотон!
		перешитать цвета
		#f12459	- оригинальный
		#ff2266	- ближайший cдвоеный
		#FF3366	- http://www.artlebedev.ru/tools/colors/ безопасные цвета -->