# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttrade', '0010_auto_20151021_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='location',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
