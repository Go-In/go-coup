# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 10:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0003_auto_20170927_0952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rightssupport',
            options={'managed': False, 'permissions': (('customer_rights', 'Global customer rights'), ('store_rights', 'Global store rights'))},
        ),
    ]
