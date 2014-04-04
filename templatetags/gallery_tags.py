# -*- coding: utf-8 -*
from django import template
register = template.Library()
from django.shortcuts import get_object_or_404

from gallery.models import Category
from gallery.models import Item


@register.simple_tag()
def gallery_category(id, tpl='gallery/__blocks/items-list.html', main=False):
	context = {}

	category = get_object_or_404(Category, id=id)
	context['category'] = category

	if main:
		context['items'] = category.get_main()
	else:
		context['items'] = category.get_public()

	tpl = template.loader.get_template(tpl)
	return tpl.render(template.Context(context))


@register.simple_tag()
def gallery_image(id, tpl='gallery/__block/item-detail.html'):
	context = {}
	try:
		context['item'] = Item.objects.get(pk=id)
	except:
		context['item'] = None

	tpl = template.loader.get_template(tpl)
	return tpl.render(template.Context(context))
