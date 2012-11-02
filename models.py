# -*- coding: utf-8 -*
from django.db import models
from datetime import datetime

from hashlib import md5
# Fields
from gallery.fields import ThumbImageField
# Translation
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import SafeUnicode

# Configuration
category_thumb_width = 185
category_thumb_height = 185
image_thumb_width = 150
image_thumb_height = 150


class Category(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, unique=True)
	url = models.SlugField(verbose_name=_('Full URL'), max_length=512, editable=False)
	parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, related_name='childs')
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500)

	description = models.TextField(verbose_name=_('Description'), null=True, blank=True)

	img = ThumbImageField(
		w=category_thumb_width,
		h=category_thumb_height,
		verbose_name=_('Image'),
		upload_to=lambda instance, filename: 'img/gallery/%s/index.%s' % (instance.url, filename.split('.')[len(filename.split('.')) - 1].lower()),
		blank=True
	)

	main = models.BooleanField(verbose_name=_('Main'))
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def image_preview(self):
		if self.img:
			return '<img src="%s" width="100">' % self.img.thumb_url
		else:
			return '(none)'
	image_preview.short_description = _('Image')
	image_preview.allow_tags = True

	def url_puth(self, this):
		if this.parent:
			return self.url_puth(this.parent) + '/' + this.slug
		else:
			return this.slug

	def display(self):
		return '&nbsp;' * (len(self.url.split('/')) - 1) * 6 + self.name
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
		return SafeUnicode('&nbsp;' * (len(self.url.split('/')) - 1) * 6 + self.name)

	class Meta:
		ordering = ['order', 'url']
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')


class Image(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	category = models.ForeignKey(Category, verbose_name=_('Category'), related_name='images', null=True, blank=True)

	def img_puth(instance, filename):
		if instance.category:
			puth = 'img/gallery/%s/%s.%s' % (instance.category.url, md5(str(datetime.now()) + filename).hexdigest(), filename.split('.')[len(filename.split('.')) - 1].lower())
		else:
			puth = 'img/gallery/%s.%s' % (md5(str(datetime.now()) + filename).hexdigest(), filename.split('.')[len(filename.split('.')) - 1].lower())
		return puth

	img = ThumbImageField(
		w=image_thumb_width,
		h=image_thumb_height,
		verbose_name=_('Image'),
		upload_to=img_puth
	)

	description = models.TextField(verbose_name=_('Description'), blank=True)

	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500, null=True, blank=True)

	def image_preview(self):
		if self.img:
			return '<img src="%s" width="150">' % self.img.thumb_url
		else:
			return '(none)'
	image_preview.short_description = _('Image')
	image_preview.allow_tags = True

	main = models.BooleanField(verbose_name=_('Main'))
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order', 'name']
		verbose_name = _('Image')
		verbose_name_plural = _('Images')
