# -*- coding: utf-8 -*
from django import template
register = template.Library()

from gallery.models import Image


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
