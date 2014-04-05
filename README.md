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
```

# Use tags
```
{% load gallery_tags %}
{% gallery_category 1 %}
{% gallery_image 1 %}
```

# Plan
	Шаблоны
		Слайдеры
		Одно изображение
		HTML 5

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
Количество просмотра для фото, галлереи, всех изображений в галлереи
Свойства и параметры через модель

# Futures
* New templates
* Optimization
* Custom template for templatetags
* README.md
* recreate thumb
* default from settings
* image filter
