#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_serverless_cron
------------

Tests for `django_serverless_cron` admin module.
"""

from django.test import TestCase
from django.utils import timezone

from django_serverless_cron.admin import run_selected_jobs
from django_serverless_cron.models import JobRun


class TestAdminRunSelectedJobs(TestCase):

    def test_run_selected_jobs_runs_jobs(self):
        # create fake job runs
        JobRun.objects.create(
            function_path='tests.example.jobs.example_job_1',
            kwargs={},
            frequency='1_second',
            time_finished_running=timezone.now()
        )
        JobRun.objects.create(
            function_path='tests.example.jobs.example_job_2',
            kwargs={},
            frequency='1_second',
            time_finished_running=timezone.now()
        )
        self.assertEqual(JobRun.objects.all().count(), 2)
        # run jobs
        run_selected_jobs(None, None, JobRun.objects.all())
        # check if the jobs ran
        self.assertEqual(JobRun.objects.all().count(), 4)
