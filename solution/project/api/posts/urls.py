import django.urls

import api.posts.views

app_name = 'api.posts'

urlpatterns = [
    django.urls.path(
        '/add',
        api.posts.views.AddPostView.as_view(),
        name='add',
    ),
]
