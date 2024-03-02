import django.urls

import api.users.views

app_name = 'api.users'

urlpatterns = [
    django.urls.path(
        '/register',
        api.users.views.RegisterView.as_view(),
        name='register',
    ),
    django.urls.path(
        '/sign-in',
        api.users.views.SignInView.as_view(),
        name='sign-in',
    ),
]
