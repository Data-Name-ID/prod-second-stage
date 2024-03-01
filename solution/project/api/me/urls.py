import django.urls

import api.me.views

app_name = 'me'

urlpatterns = [
    django.urls.path(
        'profile',
        api.me.views.ProfileView.as_view(),
        name='profile',
    ),
]
