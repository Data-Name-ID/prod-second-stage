import django.urls

import api.profiles.views

app_name = 'api.profiles'

urlpatterns = [
    django.urls.path(
        '/<str:login>',
        api.profiles.views.ProfileView.as_view(),
        name='profile',
    ),
]
