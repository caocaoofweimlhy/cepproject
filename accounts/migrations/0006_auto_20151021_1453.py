# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='contact',
            field=models.CharField(max_length=225, null=True, blank=True),
            preserve_default=True,
        ),
    ]
