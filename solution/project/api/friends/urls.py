import django.urls

import api.friends.views

app_name = 'api.friends'

urlpatterns = [
    django.urls.path(
        '/add',
        api.friends.views.AddFriendView.as_view(),
        name='add',
    ),
    django.urls.path(
        '/remove',
        api.friends.views.RemoveFriendView.as_view(),
        name='remove',
    ),
    django.urls.path(
        '',
        api.friends.views.FriendListView.as_view(),
        name='list',
    ),
]
