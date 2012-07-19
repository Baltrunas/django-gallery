# -*- coding: utf-8 -*
from django import template
register = template.Library()
from gallery.models import Category

@register.simple_tag()
def gallery_category(id, size='150x150', type='image-label-box'):
	t = template.loader.get_template('gallery_category_tag.html')
	if Category.objects.filter(pk=id).exists():
		category = Category.objects.get(pk=id)
		width = size.split('x')[0]
		height = size.split('x')[1]
	else:
		category = 404
	return t.render(template.Context({'category': category, 'id': id, 'width': width, 'height': height, 'size': size, 'type': type}))