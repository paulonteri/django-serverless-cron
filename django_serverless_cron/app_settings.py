

class Settings():
    def __init__(self, settings):
        self.SERVERLESS_CRONJOBS = getattr(settings, 'SERVERLESS_CRONJOBS', [])
