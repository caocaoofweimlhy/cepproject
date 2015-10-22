# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttrade', '0005_request_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='favor',
            name='tag',
            field=models.ManyToManyField(related_name='favors', null=True, to='ttrade.Tag', blank=True),
            preserve_default=True,
        ),
    ]
