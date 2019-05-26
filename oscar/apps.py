from django.apps import AppConfig


class OscarConfig(AppConfig):
    name = 'oscar'

    def ready(self):
        import users.signals
