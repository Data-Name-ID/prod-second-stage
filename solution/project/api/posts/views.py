import rest_framework.exceptions
import rest_framework.permissions
import rest_framework.response
import rest_framework.status
import rest_framework.views

import api.friends.models
import api.pagination
import api.posts.models
import api.posts.serializers
import api.users.models
import api.utils


class AddPostView(rest_framework.views.APIView):
    http_method_names = ('post',)
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    def post(self, request):
        serializer = api.posts.serializers.PostSerializer(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid():
            post = serializer.save()

            tag_names = request.data.get('tags', [])
            for tag_name in tag_names:
                tag, _ = api.posts.models.Tag.objects.get_or_create(
                    name=tag_name,
                )
                tag.posts.add(post)

            return rest_framework.response.Response(
                serializer.data,
                status=rest_framework.status.HTTP_201_CREATED,
            )

        return api.utils.get_error_response(serializer)


class PostDetailView(rest_framework.generics.RetrieveAPIView):
    queryset = api.posts.models.Post.objects.select_related(
        'author',
        'author__friends',
    )
    serializer_class = api.posts.serializers.PostSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    def get_object(self):
        post_id = self.kwargs.get('post_id')
        post = api.posts.models.Post.objects.get(id=post_id)

        if (
            post.author.isPublic or post.author == self.request.user
        ) or api.friends.models.Friendship.objects.filter(
            from_user=post.author,
            to_user=self.request.user,
        ).exists():
            return post

        msg = 'Указанный пост не найден либо к нему нет доступа.'
        raise rest_framework.exceptions.NotFound(msg)


class MyPostsView(rest_framework.generics.ListAPIView):
    serializer_class = api.posts.serializers.PostSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)
    pagination_class = api.pagination.Pagination

    def get_queryset(self):
        return api.posts.models.Post.objects.filter(
            author=self.request.user,
        )


class UserPostsView(rest_framework.generics.ListAPIView):
    serializer_class = api.posts.serializers.PostSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)
    pagination_class = api.pagination.Pagination

    def list(self, request, login):
        user = api.users.models.User.objects.get(login=login)
        if (
            user.isPublic or user == self.request.user
        ) or api.friends.models.Friendship.objects.filter(
            from_user=user,
            to_user=self.request.user,
        ).exists():
            return api.posts.models.Post.objects.filter(author__login=login)

        msg = 'Пользователь не найден либо к нему нет доступа..'
        raise rest_framework.exceptions.NotFound(msg)
