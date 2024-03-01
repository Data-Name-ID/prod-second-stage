import django.urls

import api.users.views

app_name = 'users'

urlpatterns = [
    django.urls.path(
        'register',
        api.users.views.RegisterView.as_view(),
        name='register',
    ),
]
