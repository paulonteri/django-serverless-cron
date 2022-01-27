# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'django_serverless_cron'
urlpatterns = [
    url(
        regex="^CronJobRun/~create/$",
        view=views.CronJobRunCreateView.as_view(),
        name='CronJobRun_create',
    ),
    url(
        regex="^CronJobRun/(?P<pk>\d+)/~delete/$",
        view=views.CronJobRunDeleteView.as_view(),
        name='CronJobRun_delete',
    ),
    url(
        regex="^CronJobRun/(?P<pk>\d+)/$",
        view=views.CronJobRunDetailView.as_view(),
        name='CronJobRun_detail',
    ),
    url(
        regex="^CronJobRun/(?P<pk>\d+)/~update/$",
        view=views.CronJobRunUpdateView.as_view(),
        name='CronJobRun_update',
    ),
    url(
        regex="^CronJobRun/$",
        view=views.CronJobRunListView.as_view(),
        name='CronJobRun_list',
    ),
	]
