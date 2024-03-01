import django.contrib.admin
import django.urls

import api.urls

urlpatterns = [
    django.urls.path('admin/', django.contrib.admin.site.urls, name='admin'),
    django.urls.path('api/', django.urls.include(api.urls)),
]
