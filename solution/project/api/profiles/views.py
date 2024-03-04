import rest_framework.permissions
import rest_framework.response
import rest_framework.status
import rest_framework.views

import api.friends.models
import api.users.models
import api.users.serializers
import api.utils


class ProfileView(rest_framework.views.APIView):
    http_method_names = ('get',)
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    def get(self, request, login):
        try:
            profile = api.users.models.User.objects.get(login=login)
        except api.users.models.User.DoesNotExist:
            return rest_framework.response.Response(
                {'reason': 'Профиль с указанным логином не существует.'},
                status=rest_framework.status.HTTP_403_FORBIDDEN,
            )

        if (
            not profile.isPublic
            and profile.login != request.user.login
            and not api.friends.models.Friendship.objects.filter(
                from_user=profile,
                to_user=request.user,
            ).exists()
        ):
            return rest_framework.response.Response(
                {'reason': 'У вас нет доступа к запрашиваемому профилю.'},
                status=rest_framework.status.HTTP_403_FORBIDDEN,
            )

        data = {
            'login': profile.login,
            'email': profile.email,
            'countryCode': profile.countryCode,
            'isPublic': profile.isPublic,
        }

        if profile.phone:
            data['phone'] = profile.phone
        if profile.image:
            data['image'] = profile.image

        return rest_framework.response.Response(
            data,
            status=rest_framework.status.HTTP_200_OK,
        )
