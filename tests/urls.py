# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.urls import re_path, include
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('django_serverless_cron.urls', namespace='django_serverless_cron')),
]
