# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20141204_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='template',
            field=models.CharField(max_length=128, null=True, verbose_name='Template', blank=True),
            preserve_default=True,
        ),
    ]
