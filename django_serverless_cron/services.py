# -*- coding: utf-8 -*-

import datetime
import logging
from typing import Dict

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.utils import timezone

from .app_settings import Settings
from .models import JobRun
from .utils import run_function_from_path

from django.conf import settings


logger = logging.getLogger(__name__)


class Job:
    """
    A class used to represent a Job that should be executed

    Attributes
    ----------
    frequency: str | None
        the frequency in which the jobs should be executed
    function_path: str
        the path to the function to be executed
    kwargs: Dict
        kwargs passed to to the function to be executed

    Methods
    -------
    run()
        Attempts to execute the job.
    """

    def __init__(self, *, frequency: str = None, function_path: str, kwargs: Dict):
        self.frequency = frequency
        self.kwargs = kwargs
        self.function_path = function_path

    @transaction.atomic
    def run(self):
        """
        Runs the job and records the job ran to the database. \n
        Jobs that are not valid to run (based on their frequency) are skipped .
        """
        logger.info(f"Running job: {self.__str__()}")
        if not self._is_valid_time_for_job_to_run():
            logger.info(f"Job terminated. Not valid time for job run: {self.__str__()}")
            return

        job_run = JobRun.objects.create(
            function_path=self.function_path,
            kwargs=self.kwargs,
            frequency=self.frequency,
        )

        try:
            with transaction.atomic():  # ?
                run_function_from_path(self.function_path, self.kwargs)
        except Exception as e:
            job_run.error = str(e)
            logger.info(f"Error running job: {str(e)}")
        else:
            job_run.time_finished_running = timezone.now()
        finally:
            job_run.save()
            logger.info(f"Job run complete: {self.__str__()}")

    def _is_valid_time_for_job_to_run(self) -> bool:
        """
        Checks whether it is a valid time to run the job based on its frequency.
        This is by checking the last run (time_attempted_running) comparing it with the current time. \n
        If the frequency is None then the job will always be run.
        """
        if not self.frequency:
            return True

        try:
            last_run = JobRun.objects.filter(
                function_path=self.function_path,
                kwargs=self.kwargs,
                frequency=self.frequency
            ).exclude(
                time_attempted_running=None
            ).latest(
                'time_attempted_running'
            )
        except ObjectDoesNotExist:
            return True
        else:
            value, unit = self.frequency.split("_")
            value = int(value)

            invalid_runs_start_time = timezone.now()\
                - datetime.timedelta(**{unit: value})

            # print("last_run.time_attempted_running", "invalid_runs_start_time")
            # print(last_run.time_attempted_running, invalid_runs_start_time)
            if last_run.time_attempted_running > invalid_runs_start_time:
                return False

            return True

    def __str__(self) -> str:
        return f"{self.function_path} {str(self.kwargs)} {self.frequency}"

    def __repr__(self) -> str:
        return self.__str__()


def run_all_jobs():
    """
    Runs all jobs defined in settings
    """
    app_settings = Settings(settings)
    jobs = [
        Job(frequency=frequency, function_path=function_path, kwargs=kwargs)
        for frequency, function_path, kwargs in app_settings.SERVERLESS_CRONJOBS
    ]

    for job in jobs:
        job.run()
