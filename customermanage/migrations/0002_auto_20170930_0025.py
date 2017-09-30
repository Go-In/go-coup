# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 00:25
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customermanage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='attribute',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='wallet',
            name='attribute',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
