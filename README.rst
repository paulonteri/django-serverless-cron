=============================
django-serverless-cron 🦡
=============================

.. image:: https://badge.fury.io/py/django-serverless-cron.svg
    :target: https://badge.fury.io/py/django-serverless-cron

.. image:: https://github.com/paulonteri/django-serverless-cron/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/paulonteri/django-serverless-cron/actions/workflows/tests.yml

.. image:: https://codecov.io/gh/paulonteri/django-serverless-cron/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/paulonteri/django-serverless-cron

.. image:: https://readthedocs.org/projects/django-serverless-cron/badge/?version=latest
     :target: http://django-serverless-cron.readthedocs.io/?badge=latest


django-serverless-cron is a Django app with a simpler approach running cron jobs.
This is done through exposing a HTTP endpoint to invoke the jobs that allows you to run any task without having to manage always-on infrastructure.

There is also an option to run jobs via management commands and the Django admin.

Why?
----

This is essentially a replacement/supplement for a traditional OS 'cron' or 'job scheduler' system:

- Serverless cron jobs no-longer a pain.
- Schedule jobs to run at a frequency that is less than 1 min. (crontab is limited to 1 min)
- The machine running crontab is no longer a single point of failure.
- The problem with the above systems is that they are often configured at the operating system level, which means their configuration is probably not easily 'portable' and 'debug-able' (if you are developing on Windows, the scheduler works differently from Linux or Unix). Also can not easily be integrated into a development environment.
- Manually triggered cron jobs. Eg: via the Django Admin.
- Alternative to cron services that aren't always available on free (and sometimes paid) web hosting services.
- Easier access to cron job execution logs and monitoring execution failures.
- No need to learn crontab. Think of it as a friendlier alternative to traditional cron jobs. Simple cron job creation. No need for cron syntax, no guessing on job frequency. Easy controls.

Documentation
-------------

Documentation is graciously hosted at https://django-serverless-cron.readthedocs.io.

Quickstart
----------

Installation
^^^^^^^^^^^^

Install Django Serverless Cron::

    pip install django-serverless-cron


Settings
^^^^^^^^

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'django_serverless_cron'
        # ...
    )

Add jobs to your settings file:

.. code-block:: python

    CRONJOBS = [
        # (
        #   '1_hours',                       # frequency (seconds, minutes, hours, days, weeks) -> in this case, every one hour
        #   'mail.jobs.send_mail_function',  # path to task/function functions -> in this case, send_mail_function()
        #   {'kwarg1': 'foo'}                # kwargs passed to the function
        # ),
        (
            '1_days',
            'your_app.services.your_job_function',
            {'kwarg1': 'foo', 'kwarg2': 'bar'}
        ),
        (
            '1_hours',
            'mail.jobs.send_mail_function',
            {"is_bulk": True}
        ),
    ]


URL patterns
^^^^^^^^^^^^
Add the jobs to your URL patterns:

.. code-block:: python

    from django_serverless_cron import urls as django_serverless_cron_urls


    urlpatterns = [
        # ...
        url(r'^', include(django_serverless_cron_urls))
        #...
    ]

Running Jobs
------------

In Development
^^^^^^^^^^^^^^

Running Jobs through HTTP requests
""""""""""""""""""""""""""""""""""

Call the `/run` path to run all jobs:

Example:

.. code-block:: bash

    curl http://localhost:8000/run

or

.. code-block:: python

    import requests

    x = requests.get('http://localhost:8000/run')


Running Jobs through the management command
"""""""""""""""""""""""""""""""""""""""""""

This will run the jobs every 30 seconds:

.. code-block:: bash

    python manage.py serverless_cron_run

You can alternatively add the `--single_run='True'` option to run the jobs just once.

In Production
^^^^^^^^^^^^^

Similar to in development, we can call the `/run` path via fully managed services which are usually ridiculously cheap. Examples:

- https://cloud.google.com/scheduler -> Great feature set, easy to use, reasonable free tier & very cheap.
- https://aws.amazon.com/eventbridge
- https://azure.microsoft.com/en-gb/services/logic-apps formerly https://docs.microsoft.com/en-us/azure/scheduler/scheduler-intro
- https://cron-job.org/en/ -> Absolutely free and open-source: https://github.com/pschlan/cron-job.org
- https://www.easycron.com
- https://cronhub.io
- https://cronless.com -> Has 30 Second Cron Jobs
- https://github.com/features/actions; https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onschedule -> eg making a HTTP request using `curl` in a step
- https://www.cronjob.de
- https://zeplo.io
- https://catalyst.zoho.com/help/cron.html
- https://www.cronjobservices.com

Related media
-------------

For more learning check out:

- https://dev.to/googlecloud/when-you-re-not-around-trigger-cloud-run-on-a-schedule-53p4 | https://youtu.be/XIwbIimM49Y
- https://aws.amazon.com/blogs/compute/using-api-destinations-with-amazon-eventbridge/
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html
- https://www.ibm.com/cloud/blog/how-to-schedule-rest-api-calls-on-ibm-cloud
- https://vercel.com/docs/concepts/solutions/cron-jobs
- https://www.dailyhostnews.com/google-cloud-launches-fully-managed-cron-job-scheduler-for-enterprises
- Cloud Scheduler from Fireship https://www.youtube.com/watch?v=WUPEUjvSBW8

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
