# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttrade', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='tag',
            field=models.ManyToManyField(related_name='requests', null=True, to='ttrade.Tag', blank=True),
            preserve_default=True,
        ),
    ]
