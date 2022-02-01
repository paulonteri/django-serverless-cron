#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_serverless_cron
------------

Tests for `django_serverless_cron` admin module.
"""

from django.test import TestCase

from django_serverless_cron.models import JobRun


class TestJobRun(TestCase):

    def test_the__str___method(self):
        function_path = 'tests.example.jobs.example_job_1'
        kwargs = {'foo': 'bar'}
        frequency = '1_second'

        job_run = JobRun.objects.create(
            function_path=function_path,
            kwargs=kwargs,
            frequency=frequency,
        )

        self.assertEqual(
            f"{function_path} {str(kwargs)} {frequency}",
            job_run.__str__()
        )
