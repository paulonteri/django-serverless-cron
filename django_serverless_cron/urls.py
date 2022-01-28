# -*- coding: utf-8 -*-


from django.conf.urls import url
from .views import RunJobsView

app_name = 'django_serverless_cron'
urlpatterns = [
    url(
        regex="^run/$",
        view=RunJobsView.as_view(),
        name='django-serverless-cron-run-jobs'
    ),
]
