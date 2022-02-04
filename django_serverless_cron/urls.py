# -*- coding: utf-8 -*-


from django.urls import re_path, path
from .views import RunJobsView, PurgeJobRunsView

app_name = 'django_serverless_cron'
urlpatterns = [
    re_path("^run/$", RunJobsView.as_view(), name='django-serverless-cron-run-jobs'),
    re_path(r'^purge-runs/(?P<n>\w+)/$', PurgeJobRunsView.as_view(), name='django-serverless-cron-purge-jobs'),
]
