import django.urls

import api.posts.views

app_name = 'api.posts'

urlpatterns = [
    django.urls.path(
        '/new',
        api.posts.views.AddPostView.as_view(),
        name='new',
    ),
    django.urls.path(
        '/<str:post_id>',
        api.posts.views.PostDetailView.as_view(),
        name='detail',
    ),
    django.urls.path(
        '/feed/my',
        api.posts.views.MyPostsView.as_view(),
        name='my-posts',
    ),
    django.urls.path(
        '/feed/<str:login>',
        api.posts.views.UserPostsView.as_view(),
        name='user-posts',
    ),
    django.urls.path(
        '/<str:post_id>/like',
        api.posts.views.LikePostView.as_view(),
        name='list',
    ),
    django.urls.path(
        '/<str:post_id>/dislike',
        api.posts.views.DislikePostView.as_view(),
        name='list',
    ),
]
