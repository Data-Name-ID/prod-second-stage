import django.contrib.admin
import django.urls
import rest_framework.routers

import countries.views
import ping.views

router = rest_framework.routers.SimpleRouter(trailing_slash=False)
router.register(r'countries', countries.views.CountriesViewSet)

urlpatterns = [
    django.urls.path('api/ping', ping.views.PingView.as_view()),
    django.urls.path('api/', django.urls.include(router.urls)),
]
