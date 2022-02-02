#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_serverless_cron
------------

Tests for `django_serverless_cron` services module.
"""

from django.test import TestCase
from django.test.utils import override_settings

from django_serverless_cron.models import JobRun
from django_serverless_cron.services import Job, RunJobs


class TestJobs(TestCase):

    def test_run_job_runs_job(self):
        self.assertEqual(JobRun.objects.all().count(), 0)
        job_one = Job(frequency="1_minutes", function_path='tests.example.jobs.example_job_1', kwargs={})
        job_one.run()
        self.assertEqual(JobRun.objects.all().count(), 1)

    def test_run_job_handles_exception(self):
        # run job
        exception_str = "Job with exception"
        job_one = Job(
            frequency="1_minutes",
            function_path='tests.example.jobs.example_job_with_exception',
            kwargs={"exception_str": exception_str}
        )
        job_one.run()
        # check job handled and saved the exception
        job = JobRun.objects.all().last()
        self.assertEqual(job.error, exception_str)

    def test_run_skips_jobs_not_valid_to_run(self):
        # run job
        job_one = Job(frequency="1_days", function_path='tests.example.jobs.example_job_1', kwargs={})
        job_one.run()
        self.assertEqual(JobRun.objects.all().count(), 1)
        # ensure the jobs didn't run again
        job_one.run()
        self.assertEqual(JobRun.objects.all().count(), 1)

    def test_is_valid_time_for_job_to_run_works(self):
        job_one = Job(frequency="1_minutes", function_path='tests.example.jobs.example_job_1', kwargs={})
        self.assertTrue(job_one._is_valid_time_for_job_to_run())
        job_one.run()
        self.assertFalse(job_one._is_valid_time_for_job_to_run())


class TestRunAllJobs(TestCase):

    @override_settings(SERVERLESS_CRONJOBS=[
        ('5_minutes', 'tests.example.jobs.example_job_1', {}),
        ('1_minutes', 'tests.example.jobs.example_job_1', {}),
    ])
    def test_run_all_jobs_runs_jobs(self):
        self.assertEqual(JobRun.objects.all().count(), 0)
        RunJobs.run_all_jobs()
        self.assertEqual(JobRun.objects.all().count(), 2)
