import django.urls

import api.me.views

app_name = 'api.me'

urlpatterns = [
    django.urls.path(
        '/profile',
        api.me.views.ProfileView.as_view(),
        name='profile',
    ),
    django.urls.path(
        '/updatePassword',
        api.me.views.UpdatePasswordView.as_view(),
        name='update-password',
    ),
]
