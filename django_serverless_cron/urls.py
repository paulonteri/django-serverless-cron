# -*- coding: utf-8 -*-


from django.urls import re_path, path
from .views import RunJobsView, purge_jobs_view

app_name = 'django_serverless_cron'
urlpatterns = [
    re_path("^run/$", RunJobsView.as_view(), name='django-serverless-cron-run-jobs'),
    path("purge/<num>/", purge_jobs_view, name='django-serverless-cron-purge-jobs'),
]
