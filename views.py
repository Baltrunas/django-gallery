# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from gallery.models import *

from django.template import RequestContext

# Локализации
from django.utils.translation import ugettext as _

# from context import context
context = {}

def category_detail(request, full_url, page=0):
	category = get_object_or_404(Category, full_url=full_url)
	image_list = Image.objects.filter(public=True, category=category.id).order_by('-created')

	context['category'] = category
	context['image_list'] = image_list
	context['title'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('gallery_detail.html', context, context_instance=RequestContext(request))