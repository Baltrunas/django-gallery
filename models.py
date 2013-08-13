# -*- coding: utf-8 -*
from django.db import models
from datetime import datetime

from hashlib import md5

# Translation
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import SafeUnicode


class Category(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, unique=True)
	url = models.SlugField(verbose_name=_('Full URL'), max_length=512, editable=False)
	parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, related_name='childs')
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500)

	description = models.TextField(verbose_name=_('Description'), null=True, blank=True)

	def upload_to(instance, filename):
		file_ext = filename.split('.')[len(filename.split('.')) - 1].lower()
		puth = 'gallery/%s/index.%s' % (instance.url, file_ext)
		return puth

	img = models.ImageField(verbose_name=_('Image'), upload_to=upload_to)

	special = models.BooleanField(verbose_name=_('Special'))
	main = models.BooleanField(verbose_name=_('Main'))

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def url_puth(self, this):
		if this.parent:
			return self.url_puth(this.parent) + '/' + this.slug
		else:
			return this.slug

	def display(self):
		display_str = SafeUnicode('&nbsp;' * (len(self.url.split('/')) - 1) * 6 + self.name)
		return display_str
	display.short_description = _('Category')
	display.allow_tags = True

	def save(self, *args, **kwargs):
		self.url = self.url_puth(self)
		super(Category, self).save(*args, **kwargs)
		for child in self.childs.all():
			child.save()

	@models.permalink
	def get_absolute_url(self):
		return ('gallery_category', (), {'url': self.url})

	def __unicode__(self):
		return self.display()

	class Meta:
		ordering = ['order', 'url']
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')


class Item(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, unique=True)
	category = models.ForeignKey(Category, verbose_name=_('Category'), related_name='items', null=True, blank=True)


	ITEM_TYPE_CHOICES = (
		('image', _('Image')),
		('video', _('Video')),
	)
	item_type = models.CharField(verbose_name=_('Item Type'), max_length=20, choices=ITEM_TYPE_CHOICES)

	def upload_to(instance, filename):
		if instance.category:
			file_folder = instance.category.url + '/' + instance.item_type
		else:
			file_folder = instance.item_type

		file_ext = filename.split('.')[len(filename.split('.')) - 1].lower()
		file_name = instance.slug

		puth = 'gallery/%s/%s.%s' % (file_folder, file_name, file_ext)
		return puth

	item_file = models.FileField(verbose_name=_('File'), upload_to=upload_to)

	description = models.TextField(verbose_name=_('Description'), blank=True)
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500, null=True, blank=True)

	main = models.BooleanField(verbose_name=_('Main'))

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	@models.permalink
	def get_absolute_url(self):
		return ('item_detail', (), {'url': self.category.url, 'id': self.id})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order', 'name']
		verbose_name = _('Gallery Item')
		verbose_name_plural = _('Gallery Items')

	# def image_preview(self):
	# 	if self.img:
	# 		img_thumbnail = get_thumbnail(self.img, '100x100', crop='center', quality=99)
	# 		return '<img src="%s" width="100">' % img_thumbnail.url
	# 	else:
	# 		return '(none)'
	# image_preview.short_description = _('Image')
	# image_preview.allow_tags = True
