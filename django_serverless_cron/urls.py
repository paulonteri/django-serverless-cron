# -*- coding: utf-8 -*-


from django.urls import re_path
from .views import RunJobsView

app_name = 'django_serverless_cron'
urlpatterns = [
    re_path(
        "^run/$",
        RunJobsView.as_view(),
        name='django-serverless-cron-run-jobs'
    ),
]
