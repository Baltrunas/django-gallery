# -*- coding: utf-8 -*
from django.contrib import admin

from gallery.models import Category
from gallery.models import Item


class ItemInline(admin.TabularInline):
	model = Item
	extra = 3


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['display', 'slug', 'order', 'main', 'public']
	search_fields = ['img', 'name', 'url', 'public']
	list_editable = ['order', 'main', 'public']
	inlines = [ItemInline]

admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'order', 'public', 'main', 'category']
	search_fields = ['name', 'order', 'public', 'main', 'category']
	list_editable = ['order', 'public', 'main', 'category']
	list_filter = ['category', 'public', 'main']

admin.site.register(Item, ItemAdmin)
