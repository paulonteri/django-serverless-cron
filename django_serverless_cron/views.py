# -*- coding: utf-8 -*-
import logging

from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.views import View

from .services import RunJobs, PurgeJobRuns

logger = logging.getLogger(__name__)


class RunJobsView(View):

    def get(self, request, *args, **kwargs):
        RunJobs.run_all_jobs()
        return HttpResponse('Done')


class PurgeJobRunsView(View):
    """
    Request triggers completed JobRun deletions
    """

    def get(self, *args, **kwargs):
        n = kwargs.get('n')
        if n is None or n == '':
            return HttpResponseBadRequest('You must supply the number of jobs to be purged.')
        try:
            PurgeJobRuns.purge_job_runs(int(n))
        except Exception as e:
            logger.exception(e, exc_info=True)
            logger.error(e)
            return HttpResponseServerError('An error occurred. Working to resolve the issue.')

        return HttpResponse(f'Last {n} jobs Purged Successfully.')
