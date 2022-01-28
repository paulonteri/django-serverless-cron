=============================
Django Serverless Cron
=============================

.. image:: https://badge.fury.io/py/django-serverless-cron.svg
    :target: https://badge.fury.io/py/django-serverless-cron

.. .. image:: https://travis-ci.org/paulonteri/django-serverless-cron.svg?branch=master
..     :target: https://travis-ci.org/paulonteri/django-serverless-cron

.. .. image:: https://codecov.io/gh/paulonteri/django-serverless-cron/branch/master/graph/badge.svg
..     :target: https://codecov.io/gh/paulonteri/django-serverless-cron

Django Serverless Cron

Documentation
-------------

The full documentation is at https://django-serverless-cron.readthedocs.io.

Features
--------

Run cron jobs easily in a serverless environment.

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
        ...
        'django_serverless_cron',
        ...
    )

Add Django Serverless Cron's cron jobs to your settings file:

.. code-block:: python

    CRONJOBS = [
        # (
        #   '1_hours', # frequency (days, minutes, hours, weeks) -> in this case, every one hour
        #   'mail.jobs.send_mail_function', # path to task/function functions -> in this case, send_mail_function()
        #   {'kwarg1': 'foo'} # kwargs passed to the function
        # ),
        (
            '1_day',
            'your_app.services.your_job_function',
            {'kwarg1': 'foo', 'kwarg2': 'bar'}
        ),
        (
            '1_hour',
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
        ...
        url(r'^', include(django_serverless_cron_urls)),
        ...
    ]


Running Jobs
^^^^^^^^^^^^

Running via the view/API
""""""""""""""""""""""""

Call the `/run` path to run all jobs:

.. code-block:: bash

    curl http://localhost:8000/run

or

.. code-block:: python

    import requests

    x = requests.get('http://localhost:8000/run')




Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
