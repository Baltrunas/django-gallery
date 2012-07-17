# django-gallery
Image gallery for django.

# Install
* Add 'gallery', to INSTALLED_APPS
* ./manage.py syncdb

# Futures
* recreate thumb
* thumb by size
* image filter
	* gallery_catgory id true true

# Changelog
## 2012.07.17
### Add
* colorbox
* templatetag gallery_image id size ('thumb' or 'original' or '__width__x__height__')


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

	цветотон
		перешитать цвета
		#f12459	- оригинальный
		#ff2266	- ближайший cдвоеный
		#FF3366	- http://www.artlebedev.ru/tools/colors/ безопасные цвета