from django import template
register = template.Library()
from django.shortcuts import get_object_or_404

from ..models import Category


@register.simple_tag()
def gallery(id, tpl='gallery/__blocks/items-list.html', main=False):
	context = {}

	category = get_object_or_404(Category, id=id)
	context['category'] = category
	context['categories'] = category.childs.all()
	context['items'] = category.get_public()

	tpl = template.loader.get_template(tpl)
	return tpl.render(template.Context(context))
