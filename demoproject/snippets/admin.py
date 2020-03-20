# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profilepost,News
# Register your models here.

admin.site.register(Profilepost)
admin.site.register(News)