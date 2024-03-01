import django.apps


class MeConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.me'
    verbose_name = 'Профиль'
