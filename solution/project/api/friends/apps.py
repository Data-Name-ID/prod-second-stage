import django.apps


class FriendsConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.friends'
    verbose_name = 'Друзья'
