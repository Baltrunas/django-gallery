from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _

from .models import Category
from .models import Item


def gallery(request):
	context = {}

	context['categories'] = Category.objects.filter(parent=None, public=True, special=False)
	context['items'] = Item.objects.filter(public=True, category=None)

	context['title'] = _('Gallery')
	context['header'] = _('Gallery')

	return render(request, 'gallery/category.html', context)


def category(request, url):
	context = {}
	category = get_object_or_404(Category, url=url, public=True, special=False)

	context['category'] = category
	context['categories'] = category.get_childs()
	context['items'] = category.get_items()

	context['title'] = category.name
	context['header'] = category.name

	if category.template:
		template = category.template
	else:
		template = 'gallery/category.html'


	return render(request, template, context)
