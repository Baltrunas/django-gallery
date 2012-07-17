# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from gallery.models import *

from django.template import RequestContext

# Локализации
from django.utils.translation import ugettext as _

# from context import context
context = {}

def category_list(request):
	categories = Category.objects.filter(parent=None, public=True).order_by('-created_at')
	images = Image.objects.filter(public=True, category=None).order_by('-created_at')

	context['categories'] = categories
	context['images'] = images
	context['title'] = 'Gallery'
	context['header'] = 'Gallery'
	context['keywords'] = 'Gallery'
	context['description'] = 'Gallery'
	return render_to_response('gallery_category.html', context, context_instance=RequestContext(request))

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
	return render_to_response('gallery_category.html', context, context_instance=RequestContext(request))
