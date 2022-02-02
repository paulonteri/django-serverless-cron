# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views import View

from .services import RunJobs


class RunJobsView(View):

    def get(self, request, *args, **kwargs):
        RunJobs.run_all_jobs()
        return HttpResponse('Done')
