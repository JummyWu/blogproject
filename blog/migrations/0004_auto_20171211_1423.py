# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-11 14:23
from __future__ import unicode_literals

from django.db import migrations
import extra_apps.DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171206_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=extra_apps.DjangoUeditor.models.UEditorField(default='', verbose_name='正文'),
        ),
    ]