# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from gallery.models import Category
from gallery.models import Item

from django.template import RequestContext

# Translation
from django.utils.translation import ugettext as _

context = {}


def category_list(request):
	categories = Category.objects.filter(parent=None, public=True, special=False).order_by('order')
	items = Item.objects.filter(public=True, category=None).order_by('order')

	context['categories'] = categories
	context['category'] = {'get_childs': categories}
	context['items'] = items
	context['title'] = _('Gallery')
	context['header'] = _('Gallery')
	return render_to_response('gallery/category.html', context, context_instance=RequestContext(request))


def category_detail(request, url, page=0):
	category = get_object_or_404(Category, url=url)
	context['category'] = category
	context['title'] = category.name
	context['header'] = category.name
	return render_to_response('gallery/category.html', context, context_instance=RequestContext(request))


def item_detail(request, url, id):
	context['item'] = get_object_or_404(Item, category__url=url, id=id)
	context['title'] = context['item'].name
	return render_to_response('gallery/item.html', context, context_instance=RequestContext(request))
