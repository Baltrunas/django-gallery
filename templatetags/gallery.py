from django.shortcuts import get_object_or_404

from django import template
register = template.Library()

from ..models import Category


@register.simple_tag()
def gallery(id, tpl='gallery/__blocks/items-list.html', main=False):
	context = {}

	category = get_object_or_404(Category, id=id)
	context['category'] = category
	context['categories'] = category.get_childs()
	context['items'] = category.get_items()

	tpl = template.loader.get_template(tpl)
	return tpl.render(template.Context(context))
