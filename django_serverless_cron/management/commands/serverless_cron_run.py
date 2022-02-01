#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from django_serverless_cron.services import run_all_jobs


class Command(BaseCommand):
    help = 'Runs all jobs defined in your settings file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--single_run', type=eval,
            choices=[True, False],
            default='False',
            help='The jobs should be executed once (instead of every 30 seconds). Default=False.'
        )

    def handle(self, *args, **kwargs):
        single_run = kwargs['single_run']

        if single_run is True:
            print("----------------------------- Jobs running once -----------------------------")
            run_all_jobs()
            return

        last_run_time = None
        while True:
            if last_run_time is None or (datetime.now() - last_run_time).seconds >= 30:
                print("----------------------- Jobs running. Will run again in 30 seconds --------------------------")
                last_run_time = datetime.now()
                run_all_jobs()

            # not run loop if in testing mode
            if settings.IS_IN_DEV_TESTING == True:
                break
