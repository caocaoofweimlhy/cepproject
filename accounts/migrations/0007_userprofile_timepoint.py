# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20151021_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='timepoint',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
    ]
