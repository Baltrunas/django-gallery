from modeltranslation.translator import translator
from modeltranslation.translator import TranslationOptions

from .models import Category
from .models import Item


class CategoryTranslation(TranslationOptions):
	fields = ['name', 'description']

translator.register(Category, CategoryTranslation)


class ItemTranslation(TranslationOptions):
	fields = ['name', 'description']

translator.register(Item, ItemTranslation)
