# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0002_rightssupport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rightssupport',
            options={'managed': False, 'permissions': (('customer_rigths', 'Global customer rights'), ('store_rights', 'Global store rights'))},
        ),
    ]
