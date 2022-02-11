from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    # connect our signal
    # this is how to configure app to know about this signal
    # in settings.py make sure app is declared as appname.app.appnameConfig to avoid issues
    def ready(self):
        import api.signals
