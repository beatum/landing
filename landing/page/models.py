# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    full_name = models.CharField(_(u'ФИО'), max_length=128)
    phone = models.CharField(_(u'Телефон'), max_length=30)
    age = models.CharField(_(u'Возраст'), max_length=3)
    position = models.CharField(_(u'Должность'), max_length=128)
    registry = models.CharField(_(u'Прописка'), max_length=256)
    yes_arrears = models.BooleanField(_(u'Нет текущих просроченных задолженностей'), default=None)
    no_arrears = models.BooleanField(_(u'Нет закрытых просроченных задолженностей более 30 дней'), default=None)
    pub_date = models.DateTimeField(_(u'Дата публикации'), auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = _(u'Заявка')
        verbose_name_plural = _(u'Заявки')

    def __unicode__(self):
        return self.full_name

    def __str__(self):
        # __unicode__ on Python 2
        return self.full_name

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)