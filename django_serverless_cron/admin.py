# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
   CronJobRun,
)


@admin.register(CronJobRun)
class CronJobRunAdmin(admin.ModelAdmin):
    pass



