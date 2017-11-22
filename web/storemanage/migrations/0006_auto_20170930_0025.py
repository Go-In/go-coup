# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 00:25
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storemanage', '0005_auto_20170928_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='attribute',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='ticket',
            name='attribute',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]