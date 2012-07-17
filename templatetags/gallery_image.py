# -*- coding: utf-8 -*
from django import template
register = template.Library()
from gallery.models import Image

@register.simple_tag()
def gallery_image(id, size='thumb'):
	t = template.loader.get_template('gallery_image_tag.html')

	if Image.objects.filter(pk=id).exists():
		image = Image.objects.get(pk=id)
		if size == 'thumb':
			image.thumb = image.img.thumb_url
		elif size == 'original':
			image.thumb = image.img.url
		else:
			size = size.split('x')
			image.thumb = image.img.thumb(int(size[0]), int(size[1]))
	else:
		image = 404
	return t.render(template.Context({'image': image, 'id': id}))
