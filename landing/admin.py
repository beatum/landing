# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group


# Remove Group from Admin
admin.site.unregister(Group)
# admin.site.unregister(Site)