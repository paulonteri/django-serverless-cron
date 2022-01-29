# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import JobRun
from .services import Job


def run_selected_jobs(modeladmin, request, queryset):
    for job_run in queryset:
        job = Job(function_path=job_run.function_path, kwargs=job_run.kwargs)
        job.run()


run_selected_jobs.short_description = 'Re-run selected jobs'


@admin.register(JobRun)
class JobRunAdmin(admin.ModelAdmin):
    list_display = (
        "function_path", "kwargs",
        "frequency", "time_attempted_running", "time_finished_running"
    )
    list_filter = ("function_path", )
    actions = (run_selected_jobs,)
