import django.urls
import rest_framework.routers

import api.countries.views
import api.ping.views
import api.users.urls

app_name = 'api'

router = rest_framework.routers.SimpleRouter(trailing_slash=False)
router.register('countries', api.countries.views.CountriesViewSet)

urlpatterns = [
    django.urls.path('', django.urls.include(router.urls)),
    django.urls.path('auth/', django.urls.include(api.users.urls)),
    django.urls.path('ping', api.ping.views.PingView.as_view()),
]
