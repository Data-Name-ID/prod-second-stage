import django.contrib.admin

import api.posts.models

django.contrib.admin.site.register(
    api.posts.models.Post,
    django.contrib.admin.ModelAdmin,
)
django.contrib.admin.site.register(
    api.posts.models.Tag,
    django.contrib.admin.ModelAdmin,
)
