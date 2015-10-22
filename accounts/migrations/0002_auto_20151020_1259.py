# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='', max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='karma',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
