# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2022-05-22 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20220522_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='fotoGalery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.FotoGalery'),
        ),
    ]
