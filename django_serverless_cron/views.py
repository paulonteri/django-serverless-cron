# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views import View

from .services import run_all_jobs


class RunJobsView(View):

    def get(self, request, *args, **kwargs):
        run_all_jobs()
        return HttpResponse('Done')
