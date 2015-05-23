# -*- coding: utf-8 -*-

from django.forms import ModelForm, TextInput, NumberInput
from django.utils.translation import ugettext_lazy as _
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['pub_date']
        widgets = {
            'full_name': TextInput(attrs={'placeholder': _(u'ФИО')}),
            'phone': TextInput(attrs={'placeholder': _(u'Телефон')}),
            'age': TextInput(attrs={'placeholder': _(u'Возраст')}),
            'position': TextInput(attrs={'placeholder': _(u'Должность')}),
            'registry': TextInput(attrs={'placeholder': _(u'Прописка')}),
        }