# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from gallery.models import Category
from gallery.models import Image

from django.template import RequestContext

# Translation
from django.utils.translation import ugettext as _

context = {}


def category_list(request):
	categories = Category.objects.filter(parent=None, public=True).order_by('-created_at')
	images = Image.objects.filter(public=True, category=None).order_by('-created_at')

	context['categories'] = categories
	context['images'] = images
	context['title'] = _('Gallery')
	context['header'] = _('Gallery')
	context['keywords'] = _('Gallery')
	context['description'] = _('Gallery')
	return render_to_response('gallery/category.html', context, context_instance=RequestContext(request))


def category_detail(request, url, page=0):
	category = get_object_or_404(Category, url=url)
	categories = Category.objects.filter(parent=category.pk, public=True).order_by('-created_at')
	images = Image.objects.filter(public=True, category=category.pk).order_by('-created_at')

	context['categories'] = categories
	context['images'] = images
	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('gallery/category.html', context, context_instance=RequestContext(request))


def item_detail(request, id):
	context['image'] = get_object_or_404(Image, id=id)
	context['title'] = context['image']
	return render_to_response('gallery/item_detail.html', context, context_instance=RequestContext(request))
