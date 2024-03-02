import django.apps


class PostsConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.posts'
    verbose_name = 'Посты'
