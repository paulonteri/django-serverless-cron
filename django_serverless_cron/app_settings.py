from django.conf import settings

SERVERLESS_CRONJOBS = getattr(settings, 'SERVERLESS_CRONJOBS', [])
