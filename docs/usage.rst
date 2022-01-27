=====
Usage
=====

To use Django Serverless Cron in a project, add it to your `INSTALLED_APPS`:

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
