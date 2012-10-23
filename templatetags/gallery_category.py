# -*- coding: utf-8 -*
from django.template import Library
from django.template import loader
register = Library()

from gallery.models import Category


@register.simple_tag()
def gallery_category(id, size='150x150', type='image-label-box'):
	template = loader.get_template('gallery/category_tag.html')
	try:
		category = Category.objects.get(pk=id)
		width = size.split('x')[0]
		height = size.split('x')[1]
	except:
		category = 404
	return template.render(template.Context({'category': category, 'id': id, 'width': width, 'height': height, 'size': size, 'type': type}))
