#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_serverless_cron
------------

Tests for `django_serverless_cron` views module.
"""

from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse

from django_serverless_cron.models import JobRun


class TestRunJobsView(TestCase):

    @override_settings(SERVERLESS_CRONJOBS=[
        ('5_minutes', 'tests.example_jobs.example_job_1', {}),
        ('1_minutes', 'tests.example_jobs.example_job_1', {}),
    ])
    def test_run_jobs_view_runs_jobs(self):
        self.assertEqual(JobRun.objects.all().count(), 0)
        url = reverse("django_serverless_cron:django-serverless-cron-run-jobs")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(JobRun.objects.all().count(), 2)
