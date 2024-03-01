import django.contrib.admin
import django.contrib.auth.admin
import django.contrib.auth.models

import api.users.models

django.contrib.admin.site.register(
    api.users.models.User,
    django.contrib.admin.ModelAdmin,
)
