# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2022-05-22 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20220512_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='foto/')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.UserPortal')),
            ],
            options={
                'ordering': ('create_at',),
            },
        ),
        migrations.CreateModel(
            name='FotoGalery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('sort_index', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='newspost',
            options={'ordering': ('show_at',)},
        ),
        migrations.AddField(
            model_name='fotogalery',
            name='subdivision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Subdivision'),
        ),
        migrations.AddField(
            model_name='foto',
            name='fotoGalery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Subdivision'),
        ),
    ]
