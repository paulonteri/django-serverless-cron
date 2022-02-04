# -*- coding: utf-8 -*-
import logging

from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.views import View

from .services import RunJobs, purge_jobs

logger = logging.getLogger(__name__)


class RunJobsView(View):

    def get(self, request, *args, **kwargs):
        RunJobs.run_all_jobs()
        return HttpResponse('Done')


def purge_jobs_view(request, num):
    n = request.GET.get(num)
    if n is None:
        return HttpResponseBadRequest('You must supply the number of jobs to be purged.')
    try:
        purge_jobs(n)
        return HttpResponse(f'Last {n} jobs Purged Successfully.')
    except Exception as e:
        logger.exception(e, exc_info=True)
        logger.error(e)
        HttpResponseServerError('An error occurred. Working to resolve the issue.')
