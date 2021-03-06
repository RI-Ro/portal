# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2022-05-09 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=500)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('body', models.TextField(verbose_name='\u041d\u043e\u0432\u043e\u0441\u0442\u044c')),
                ('prev_image', models.ImageField(blank=True, null=True, upload_to='articles/', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430-\u0430\u043d\u043e\u043d\u0441')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('show_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PortalAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Razdel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPortal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='newspost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.PortalAdmin'),
        ),
        migrations.AddField(
            model_name='newspost',
            name='razdel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Razdel'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='news.NewsPost'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.UserPortal'),
        ),
    ]
