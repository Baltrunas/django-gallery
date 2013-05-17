# django-gallery
Images gallery for django.

# Required
* sorl.thumbnail
* jQuery

# Install
* Add 'gallery', to INSTALLED_APPS
* url(r'^gallery/', include('gallery.urls')),
* ./manage.py syncdb

```html
	<link rel="stylesheet" href="/static/colorboxcolorbox.css">
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

# Use tags

```
	{% load gallery %}
	{% gallery_category 2 '200x130' %}
```

# Plan
	- Перейти к использованию sorl
		+ item_detail.html
		- category.html
		- category_tag.html
		- detail.html
		- image_tag.html

	Шаблоны
		Слайдеры
		Одно изображение
		HTML 5

	- Перевести все стили в bem
	- Вынести все стили и js и images в static

	- Добавать к категориям выбор шаблона.
		Шаблон это модель, содержашяя текст шаблона наследуется от файла
		Один из шаблонов назначается как дефолтный
		Если ни один из шаблонов не назначен шаблоном по умолчанию то
		используется файл
			name
			base
			description
			html-text
			default
			public
			created_at
			updated_at

	Добавить к изображениям технические данные
		дата снимка
		дата обрабоки
		диафрагма
		выдержка
		фокусное растояние
		исо
		камера
	- Настройка указания заголовков и хлебных крошек?

	- Add image_preview

	В галлереи конечным является изображение
	В портфолио конечным является проект, который может содержать несколько изображений...

Если высота больше обрезка по верху
Для категории пометка проект
Для шаблона тип категория проект или изображение
Количество просмотра для фото, галлереи, всех изображений в галлереи
Свойства и тара метры через модель

# Futures
* New templates
* Optimization
* Custom template for templatetags
* README.md
* recreate thumb
* default from settings
* image filter

# Changelog
## 2013.03.24
### Add
* Image detail page
### Changes
* Thumbnail to sorl.thumbnail
### Delete
* colorbox
* fields.py

## 2012.11.02
### Add
* Locale translation
### Fix
* Template optimization 

## 2012.07.19
### Add
* templatetag gallery_category id size type ('thumb' or 'original' or 'WIDTHxHEIGHT')

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