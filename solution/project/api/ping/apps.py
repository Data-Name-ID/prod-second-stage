import django.apps


class PingConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.ping'
    verbose_name = 'Пинг'
