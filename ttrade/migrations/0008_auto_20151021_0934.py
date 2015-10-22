# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20151021_0924'),
        ('ttrade', '0007_remove_favor_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='accepted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request',
            name='acceptor',
            field=models.ForeignKey(related_name='request_acceptor', blank=True, to='accounts.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.ForeignKey(related_name='request_user', blank=True, to='accounts.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
