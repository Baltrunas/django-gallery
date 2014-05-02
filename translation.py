# -*- coding: utf-8 -*-
# Model Translation
from modeltranslation.translator import translator
from modeltranslation.translator import TranslationOptions

# Models
from .models import Category
from .models import Item


class CategoryTranslationOptions(TranslationOptions):
	fields = ['name', 'description']

translator.register(Category, CategoryTranslationOptions)


class ItemTranslationOptions(TranslationOptions):
	fields = ['name', 'description']

translator.register(Item, ItemTranslationOptions)