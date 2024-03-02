import django.urls
import rest_framework.routers

import api.countries.views
import api.friends.urls
import api.me.urls
import api.ping.views
import api.profiles.urls
import api.users.urls

app_name = 'api'

router = rest_framework.routers.SimpleRouter(trailing_slash=False)
router.register('countries', api.countries.views.CountriesViewSet)

urlpatterns = [
    django.urls.path('', django.urls.include(router.urls)),
    django.urls.path('auth', django.urls.include(api.users.urls)),
    django.urls.path('ping', api.ping.views.PingView.as_view()),
    django.urls.path('me', django.urls.include(api.me.urls)),
    django.urls.path('profile', django.urls.include(api.profiles.urls)),
    django.urls.path('friends', django.urls.include(api.friends.urls)),
]
