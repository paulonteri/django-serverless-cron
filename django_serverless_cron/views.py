# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	CronJobRun,
)


class CronJobRunCreateView(CreateView):

    model = CronJobRun


class CronJobRunDeleteView(DeleteView):

    model = CronJobRun


class CronJobRunDetailView(DetailView):

    model = CronJobRun


class CronJobRunUpdateView(UpdateView):

    model = CronJobRun


class CronJobRunListView(ListView):

    model = CronJobRun

