# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttrade', '0006_favor_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favor',
            name='tag',
        ),
    ]
