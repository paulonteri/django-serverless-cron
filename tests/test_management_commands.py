#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_serverless_cron
------------

Tests for `django_serverless_cron` management commands.
"""

from django.test import TestCase
from django.test.utils import override_settings

from django_serverless_cron.management.commands.serverless_cron_run import Command as RunCommand
from django_serverless_cron.management.commands.serverless_cron_purge import Command as PurgeCommand
from django_serverless_cron.models import JobRun


class TestCommandServerlessCronRun(TestCase):

    @override_settings(SERVERLESS_CRONJOBS=[
        ('5_minutes', 'tests.example.jobs.example_job_1', {}),
        ('1_minutes', 'tests.example.jobs.example_job_2', {}),
        ('5_minutes', 'tests.example.jobs.example_job_2', {}),
    ])
    def test_serverless_cron_run_command_handle(self):
        self.assertEqual(JobRun.objects.all().count(), 0)
        command = RunCommand()
        command.handle(single_run=False)
        self.assertEqual(JobRun.objects.all().count(), 3)

    @override_settings(SERVERLESS_CRONJOBS=[
        ('5_minutes', 'tests.example.jobs.example_job_1', {}),
        ('1_minutes', 'tests.example.jobs.example_job_2', {}),
        ('5_minutes', 'tests.example.jobs.example_job_2', {}),
    ])
    def test_serverless_cron_run_command_handle_single_run(self):
        self.assertEqual(JobRun.objects.all().count(), 0)
        command = RunCommand()
        command.handle(single_run=True)
        self.assertEqual(JobRun.objects.all().count(), 3)


class TestCommandServerlessCronPurge(TestCase):
    @override_settings(SERVERLESS_CRONJOBS=[
        ('5_minutes', 'tests.example.jobs.example_job_1', {}),
        ('1_minutes', 'tests.example.jobs.example_job_2', {}),
        ('5_minutes', 'tests.example.jobs.example_job_2', {}),
    ])
    def test_serverless_cron_purge_handle_single_run(self):
        self.assertEqual(JobRun.objects.all().exists(), False)
        run_command = RunCommand()
        run_command.handle(single_run=True)
        self.assertEqual(JobRun.objects.all().exists(), True)
        command = PurgeCommand()
        command.handle(n=2)
        self.assertEqual(JobRun.objects.all().count(), 1)
