# -*- coding: utf-8 -*
from django import template
register = template.Library()

from gallery.models import Category


@register.simple_tag()
def gallery_category(id, size='150x150', type='image-label-box'):
	tpl = template.loader.get_template('gallery/category_tag.html')
	try:
		category = Category.objects.get(pk=id)
		width = size.split('x')[0]
		height = size.split('x')[1]
	except:
		category = 404
	return tpl.render(template.Context({'category': category, 'id': id, 'width': width, 'height': height, 'size': size, 'type': type}))
