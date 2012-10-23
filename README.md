# django-gallery
Images gallery for django.

# Install
* Add 'gallery', to INSTALLED_APPS
* url(r'^gallery/', include('gallery.urls')),
* ./manage.py syncdb

```html
	<link rel="stylesheet" href="/static/colorboxcolorbox.css" />
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
	<script src="/static/colorbox/jquery.colorbox.js"></script>
	<script>
		$(document).ready(function(){
			$("a").colorbox({rel:'colorbox', slideshow:true});
			$("#click").click(function(){ 
				$('#click').css({"background-color":"#f00", "color":"#fff", "cursor":"inherit"}).text("Open this window again and this messagwill still be 	here.");
				return false;
			});
		});
	</script>
```


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