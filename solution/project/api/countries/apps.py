import django.apps


class CountriesConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.countries'
    verbose_name = 'Страны'
