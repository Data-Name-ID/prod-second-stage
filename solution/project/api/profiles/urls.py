import django.urls

import api.me.views

app_name = 'api.profiles'

urlpatterns = [
    django.urls.path(
        '/<str:login>',
        api.me.views.ProfileView.as_view(),
        name='profile',
    ),
]
