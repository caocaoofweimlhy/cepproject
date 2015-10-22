# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttrade', '0008_auto_20151021_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='duration',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
