# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'position', 'registry', 'age', 'yes_arrears', 'no_arrears', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['full_name']

admin.site.register(Person, PersonAdmin)
