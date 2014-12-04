from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _

from .models import Category
from .models import Item


def gallery(request):
	context = {}
	categories = Category.objects.filter(parent=None, public=True, special=False).order_by('order')
	items = Item.objects.filter(public=True, category=None).order_by('order')

	context['categories'] = categories
	context['items'] = items
	context['title'] = _('Gallery')
	context['header'] = _('Gallery')
	return render(request, 'gallery/category.html', context)


def category(request, url):
	context = {}
	category = get_object_or_404(Category, url=url, public=True, special=False)
	context['category'] = category
	context['title'] = category.name
	context['header'] = category.name
	return render(request, 'gallery/category.html', context)
