# -*- coding: utf-8 -*
from django.contrib import admin
from gallery.models import Category
from gallery.models import Image


class PriceInline(admin.TabularInline):
	model = Image
	extra = 0


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('display', 'slug', 'url', 'order', 'main', 'public')
	search_fields = ('img', 'name', 'url', 'public')
	list_editable = ['order', 'main', 'public']
	inlines = [PriceInline]


class ImageAdmin(admin.ModelAdmin):
	list_display = ('name', 'public', 'main', 'category')
	search_fields = ('name', 'public', 'main', 'category')
	list_editable = ('public', 'main', 'category')
	list_filter = ('category', 'public', 'main')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
