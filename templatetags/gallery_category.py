# -*- coding: utf-8 -*
from django import template
register = template.Library()

from gallery.models import Category
from gallery.models import Image


@register.simple_tag()
def gallery_category(id, size='150x150', type='image-label-box', main=False):
	context = {}
	context['id'] = id
	context['type'] = type
	context['size'] = size
	tpl = template.loader.get_template('gallery/category_tag.html')
	try:
		context['category'] = Category.objects.get(pk=id, public=True)
		if main:
			context['category_images'] = Image.objects.filter(category=id, public=True, main=True)
		else:
			context['category_images'] = Image.objects.filter(category=id, public=True)
		context['width'] = size.split('x')[0]
		context['height'] = size.split('x')[1]
	except:
		context['category'] = 404
	return tpl.render(template.Context(context))
