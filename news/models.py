# /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789-_",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA0123456789-_")

tr = {ord(a):ord(b) for a, b in zip(*symbols)}

class Subdivision(models.Model):
    title = models.CharField(max_length=150)
    sort_index = models.PositiveIntegerField()

    def __unicode__(self):
        return self.title

class UserPortal(User):
    admin = models.BooleanField(default=False)

class Razdel(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.translate(tr))

        super(Razdel, self).save(*args, **kwargs)

class TypeNews(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.translate(tr))

        super(TypeNews, self).save(*args, **kwargs)

class NewsPost(models.Model):
    title = models.CharField(u'Описание новости', max_length=300)
    slug = models.SlugField(null=True, blank=True)
    body = models.TextField(u'Новость')
    prev_image = models.ImageField(u'Картинка-анонс', upload_to='articles/', blank=True, null=True)
    author = models.ForeignKey(UserPortal, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    show_at = models.DateTimeField()
    type = models.ForeignKey(TypeNews, on_delete=models.SET_NULL, null=True)
    razdel = models.ForeignKey(Razdel, on_delete=models.SET_NULL, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.translate(tr))
        super(NewsPost, self).save(*args, **kwargs)

    def get_all_comment(self):
        return self.comment.all()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('show_at',)


class Comment(models.Model):
    user = models.ForeignKey(UserPortal, on_delete=models.SET_NULL, null=True)
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(NewsPost, related_name="comment", on_delete=models.CASCADE)

class FotoGalery(models.Model):
    title = models.CharField(max_length=250)
    subdivision = models.ForeignKey(Subdivision, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

class Foto(models.Model):
    title = models.CharField(max_length=250)
    fotoGalery = models.ForeignKey(FotoGalery, blank=True, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(UserPortal, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='foto/')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = u'Фотография_{}'.format(self.id)
        super(Foto, self).save(*args, **kwargs)

    class Meta:
        ordering = ('create_at',)
