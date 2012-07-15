# -*- coding: utf-8 -*
from django.db import models
from datetime import datetime

from md5 import md5
# Поля
from gallery.fields import ThumbImageField

# Локализации
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	slug = models.SlugField(verbose_name=_('URL'), max_length=128, unique=True, help_text=_('URL Simbols only slug'))
	url = models.SlugField(verbose_name=_('Full URL'), max_length=512, editable=False)
	parent = models.ForeignKey('self', verbose_name=_('childs'), null=True, blank=True, db_index=True, related_name='child_set')
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500)
	
	description = models.TextField(
		verbose_name=_('Description'),
		help_text=_('''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_text');">ON \ OFF</a>'''),
		null=True,
		blank=True
	)
	
	img = ThumbImageField(
		w = 185,
		h = 185,
		verbose_name=_('Image'),
		upload_to=lambda instance, filename: 'img/gallery/%s/index.%s' % (instance.url, filename.split('.')[len(filename.split('.'))-1].lower()),
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

	def puth (self, id):
		puth = Category.objects.get(pk=id).name
		if not Category.objects.get(pk=id).parent:
			return puth
		else:
			return self.puth(Category.objects.get(pk=Category.objects.get(pk=id).parent.id).id) + u' → ' + puth

	def url_puth (self, id):
		url_puth = Category.objects.get(pk=id).url
		if not Category.objects.get(pk=id).parent:
			return url_puth
		else:
			return self.url_puth(Category.objects.get(pk=Category.objects.get(pk=id).parent.id).id) + '/' + url_puth

	def save(self, *args, **kwargs):
		super(Category, self).save(*args, **kwargs)
		# self.full_url = '/' + self.url_puth(self.id) + '/'
		
		self.full_url = self.url_puth(self.id)
		super(Category, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return '/gallery/' + self.full_url + '/'
	
	def __unicode__(self):
		return self.puth(self.id)

	class Meta:
		ordering = ['order', 'full_url']
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')

class Image(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	category = models.ForeignKey(Category, verbose_name=_('Category'))
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500)
	
	description = models.TextField(
		verbose_name=_('Text'),
		help_text=_('''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_text');">ON \ OFF</a>'''),
		blank=True,
		editable=False,
		default='-'
	)

	img = ThumbImageField(
		w = 150,
		h = 150,
		verbose_name=_('Image'),
		upload_to=lambda instance, filename: 'img/gallery/%s/%s.%s' % (instance.category.url, md5(str(datetime.now()) + filename).hexdigest(), filename.split('.')[len(filename.split('.'))-1].lower()),
		blank=True,
		help_text = 'height: 467px and width: 700px'
	)
	
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