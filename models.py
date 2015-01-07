from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import SafeUnicode


def gallery_upload_to(instance, filename):
	file_type = filename.split('.')[len(filename.split('.')) - 1].lower()
	puth = 'gallery/%s/index.%s' % (instance.url, file_type)
	return puth

class Category(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, unique=True)
	url = models.SlugField(verbose_name=_('Full URL'), max_length=512, editable=False)
	parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, related_name='childs')
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500)

	description = models.TextField(verbose_name=_('Description'), null=True, blank=True)

	img = models.ImageField(verbose_name=_('Image'), upload_to=gallery_upload_to)

	width = models.PositiveIntegerField(verbose_name=_('Width'), null=True, blank=True)
	height = models.PositiveIntegerField(verbose_name=_('Height'), null=True, blank=True)

	template = models.CharField(verbose_name=_('Template'), max_length=128, null=True, blank=True)

	special = models.BooleanField(verbose_name=_('Special'), default=False)

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

	def get_childs(self):
		return self.childs.filter(public=True, special=False)

	def get_items(self):
		return self.items.filter(public=True)

	def size(self):
		if self.width and self.height:
			return '%sx%s' % (self.width, self.height)
		elif self.width:
			return '%s' % (self.width)
		elif self.height:
			return 'x%s' % (self.height)
		else:
			return ''

	@models.permalink
	def get_absolute_url(self):
		return ('gallery_category', (), {'url': self.url})

	def __unicode__(self):
		return self.display()

	class Meta:
		ordering = ['order', 'url']
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')


def item_upload_to(instance, filename):
	if instance.category:
		file_folder = instance.category.url + '/' + instance.item_type
	else:
		file_folder = instance.item_type

	puth = 'gallery/%s/%s' % (file_folder, filename)
	return puth

class Item(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	category = models.ForeignKey(Category, verbose_name=_('Category'), related_name='items', null=True, blank=True)

	ITEM_TYPE_CHOICES = (
		('image', _('Image')),
		('video', _('Video')),
	)
	item_type = models.CharField(verbose_name=_('Item Type'), max_length=20, default='image', choices=ITEM_TYPE_CHOICES)

	item_file = models.FileField(verbose_name=_('File'), upload_to=item_upload_to)

	description = models.TextField(verbose_name=_('Description'), blank=True)
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500, null=True, blank=True)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

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
