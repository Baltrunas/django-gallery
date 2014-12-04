# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.gallery.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=128, verbose_name='Slug')),
                ('url', models.SlugField(verbose_name='Full URL', max_length=512, editable=False)),
                ('order', models.PositiveSmallIntegerField(default=500, verbose_name='Order')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('img', models.ImageField(upload_to=apps.gallery.models.gallery_upload_to, verbose_name='Image')),
                ('width', models.PositiveIntegerField(null=True, verbose_name='Width', blank=True)),
                ('height', models.PositiveIntegerField(null=True, verbose_name='Height', blank=True)),
                ('special', models.BooleanField(default=False, verbose_name='Special')),
                ('main', models.BooleanField(default=False, verbose_name='Main')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('parent', models.ForeignKey(related_name='childs', verbose_name='Parent', blank=True, to='gallery.Category', null=True)),
            ],
            options={
                'ordering': ['order', 'url'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('item_type', models.CharField(default=b'image', max_length=20, verbose_name='Item Type', choices=[(b'image', 'Image'), (b'video', 'Video')])),
                ('item_file', models.FileField(upload_to=apps.gallery.models.item_upload_to, verbose_name='File')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=500, null=True, verbose_name='Order', blank=True)),
                ('main', models.BooleanField(default=False, verbose_name='Main')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('category', models.ForeignKey(related_name='items', verbose_name='Category', blank=True, to='gallery.Category', null=True)),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name': 'Gallery Item',
                'verbose_name_plural': 'Gallery Items',
            },
            bases=(models.Model,),
        ),
    ]
