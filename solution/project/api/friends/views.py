import rest_framework.generics
import rest_framework.permissions
import rest_framework.response
import rest_framework.status
import rest_framework.views

import api.friends.models
import api.friends.serializers
import api.pagination
import api.users.models
import api.utils


class AddFriendView(rest_framework.views.APIView):
    http_method_names = ('post',)
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    def post(self, request):
        if (
            api.users.models.User.objects.filter(
                login=request.data.get('login'),
            )
            .exclude(id=request.user.id)
            .exists()
        ):
            request.user.add_friend(request.data.get('login'))
            return rest_framework.response.Response(
                {'status': 'ok'},
                status=rest_framework.status.HTTP_200_OK,
            )

        return rest_framework.response.Response(
            {'reason': 'Пользователь с указанным логином не найден.'},
            status=rest_framework.status.HTTP_404_NOT_FOUND,
        )


class RemoveFriendView(rest_framework.views.APIView):
    http_method_names = ('post',)
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    def post(self, request):
        request.user.remove_friend(request.data.get('login'))
        return rest_framework.response.Response(
            {'status': 'ok'},
            status=rest_framework.status.HTTP_200_OK,
        )


class FriendListView(rest_framework.generics.ListAPIView):
    http_method_names = ('get',)
    serializer_class = api.friends.serializers.FriendsSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)
    pagination_class = api.pagination.Pagination

    def get_queryset(self):
        return api.friends.models.Friendship.objects.filter(
            from_user=self.request.user,
        )
