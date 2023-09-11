from django.apps import AppConfig


class NewspaperappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newspaperapp'

    def ready(self):
        import newspaperapp.signals
