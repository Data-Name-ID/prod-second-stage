import rest_framework.permissions
import rest_framework.response
import rest_framework.status
import rest_framework.views

import api.users.models
import api.users.serializers
import api.utils


class ProfileView(rest_framework.views.APIView):
    http_method_names = ('get', 'patch')
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    def get(self, request):
        return api.utils.get_profile_response(request)

    def patch(self, request):
        serializer = api.users.serializers.UserSerializer(
            request.user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            if not api.utils.check_country_code(
                request.data.get('countryCode'),
            ):
                return rest_framework.response.Response(
                    {'reason': 'Некорректный код страны.'},
                    status=rest_framework.status.HTTP_400_BAD_REQUEST,
                )

            if (
                api.users.models.User.objects.exclude(login=request.user.login)
                .filter(
                    phone=request.data.get('phone'),
                )
                .exists()
            ):
                msg = 'Пользователь с данным телефоном уже зарегистрирован.'
                return rest_framework.response.Response(
                    {'reason': msg},
                    status=rest_framework.status.HTTP_409_CONFLICT,
                )

            serializer.save()
            return api.utils.get_profile_response(request)

        return api.utils.get_error_response(serializer)
