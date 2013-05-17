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


@register.simple_tag()
def gallery_image(id, size='thumb', type='image'):
	tpl = template.loader.get_template('gallery/image_tag.html')
	try:
		image = Image.objects.get(pk=id)
		if size == 'thumb':
			width = 150
			height = 150
			image.url = image.img.thumb_url
		elif size == 'original':
			image.url = image.img.url
		else:
			size = size.split('x')
			width = size[0]
			height = size[1]
			image.url = image.img.thumb(int(size[0]), int(size[1]))
		if type == 'url':
			return image.url
	except:
		image = 404
	return tpl.render(template.Context({'image': image, 'id': id, 'size': size, 'type': type, 'width': width, 'height': height}))
