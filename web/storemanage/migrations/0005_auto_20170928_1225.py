# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storemanage', '0004_ticket_expire_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='content_image_url',
            field=models.CharField(max_length=1023, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_image_url',
            field=models.CharField(max_length=1023, null=True),
        ),
    ]
