# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_dailys'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailys',
            name='title',
            field=models.CharField(default='default title', max_length=100, unique=True),
        ),
    ]