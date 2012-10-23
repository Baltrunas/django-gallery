# -*- coding: utf-8 -*
from django.contrib import admin
from gallery.models import Category
from gallery.models import Image


class PriceInline(admin.TabularInline):
	model = Image
	extra = 0


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('display', 'slug', 'url', 'order', 'main', 'public', 'image_preview')
	search_fields = ('img', 'name', 'url', 'public')
	list_editable = ['order', 'main', 'public']
	inlines = [PriceInline]


class ImageAdmin(admin.ModelAdmin):
	list_display = ('name', 'public', 'category', 'image_preview')
	search_fields = ('name', 'public', 'category')
	list_editable = ('public',)
	list_filter = ('category', 'public',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
