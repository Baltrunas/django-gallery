# -*- coding: utf-8 -*
from django import template
register = template.Library()

from gallery.models import Item


@register.simple_tag()
def gallery_category(id):
	context = {}
	context['id'] = id
	context['items'] = Item.objects.filter(category=id, public=True)

	tpl = template.loader.get_template('gallery/__blocks/items-list.html')
	return tpl.render(template.Context(context))


@register.simple_tag()
def gallery_image(id):
	context = {}
	try:
		context['item'] = Item.objects.get(pk=id)
	except:
		context['item'] = None

	tpl = template.loader.get_template('gallery/item-detail.html')
	return tpl.render(template.Context(context))
