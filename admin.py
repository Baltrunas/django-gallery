# -*- coding: utf-8 -*
from django.contrib import admin
from gallery.models import *

from django import forms



class PriceInline(admin.TabularInline):
	model = Image
	extra = 0
	
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('display', 'slug', 'url', 'order', 'main', 'public', 'image_preview')
	search_fields = ('img', 'name', 'url', 'public')
	list_editable = ['order', 'main', 'public']
	inlines = [PriceInline]
	class Media:
		js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textareas.js',)


class ImageAdmin(admin.ModelAdmin):
	list_display = ('name', 'public', 'category', 'image_preview')
	search_fields = ('name', 'public', 'category')
	list_editable = ('public',)
	list_filter = ('category', 'public',)
	class Media:
		js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textareas.js',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
