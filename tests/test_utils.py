#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_serverless_cron
------------

Tests for `django_serverless_cron` utils module.
"""

from django.test import TestCase

from django_serverless_cron.utils import run_function_from_path


def function_that_returns_true(**kwargs):
    """Function that is used to test the run_function_from_path function"""
    return True


class TestRunFunctionFromPath(TestCase):

    def test_run_function_from_path_runs_function(self):
        result = run_function_from_path('tests.test_utils.function_that_returns_true', {})
        self.assertTrue(result)
