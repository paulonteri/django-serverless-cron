# -*- coding: utf-8 -*-


from django.conf.urls import url
from .views import MyView

app_name = 'django_serverless_cron'
urlpatterns = [
    url(
        regex="^run/$",
        view=MyView.as_view(),
        name='run-serverless-cron-jobs'
    ),
]
