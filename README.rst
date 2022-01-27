=============================
Django Serverless Cron
=============================

.. image:: https://badge.fury.io/py/django-serverless-cron.svg
    :target: https://badge.fury.io/py/django-serverless-cron

.. image:: https://travis-ci.org/paulonteri/django-serverless-cron.svg?branch=master
    :target: https://travis-ci.org/paulonteri/django-serverless-cron

.. image:: https://codecov.io/gh/paulonteri/django-serverless-cron/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/paulonteri/django-serverless-cron

Django Serverless Cron

Documentation
-------------

The full documentation is at https://django-serverless-cron.readthedocs.io.

Quickstart
----------

Install Django Serverless Cron::

    pip install django-serverless-cron

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_serverless_cron.apps.DjangoServerlessCronConfig',
        ...
    )

Add Django Serverless Cron's URL patterns:

.. code-block:: python

    from django_serverless_cron import urls as django_serverless_cron_urls


    urlpatterns = [
        ...
        url(r'^', include(django_serverless_cron_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
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
