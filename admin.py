from django.contrib import admin

from .models import Category
from .models import Item


class ItemInline(admin.TabularInline):
	model = Item
	extra = 3


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['display', 'slug', 'order', 'public']
	search_fields = ['img', 'name', 'url', 'public']
	list_editable = ['order', 'public']
	inlines = [ItemInline]

admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'order', 'public', 'category']
	search_fields = ['name', 'order', 'public', 'category']
	list_editable = ['order', 'public', 'category']
	list_filter = ['category', 'public']

admin.site.register(Item, ItemAdmin)
