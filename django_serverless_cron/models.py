# -*- coding: utf-8 -*-

import uuid

from django.db import models
from django.utils import timezone


class JobRun(models.Model):
    """
    Django model that stores all job executions
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    function_path = models.CharField(
        max_length=255,
        help_text="The path to the function executed."
    )
    kwargs = models.JSONField(
        null=True, blank=True,
        help_text="The kwargs to passed to the function."
    )
    frequency = models.CharField(
        max_length=255, null=True, blank=True,
        help_text="The frequency that was set for the job."
    )
    # is_running = models.BooleanField(
    #     default=False,
    #     help_text="Whether the job is currently running."
    # )
    time_attempted_running = models.DateTimeField(
        default=timezone.now,
        help_text="Time when first attempted to run the job"
    )
    time_finished_running = models.DateTimeField(
        null=True, blank=True,
        help_text="Time when the job finished running"
    )
    error = models.TextField(null=True, blank=True)

    objects = models.Manager()

    class Meta:
        ordering = ('-time_attempted_running',)

    def __str__(self):
        return f"{self.function_path} {str(self.kwargs)} {self.frequency}"
