import django.contrib.auth.hashers
import rest_framework.permissions
import rest_framework.response
import rest_framework.status
import rest_framework.views

import api.me.serializers
import api.users.models
import api.users.serializers
import api.utils


class ProfileView(rest_framework.views.APIView):
    http_method_names = ('get', 'patch')
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    def get(self, request):
        return api.utils.get_profile_response(request)

    def patch(self, request):
        serializer = api.me.serializers.UserSerializer(
            request.user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
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


class UpdatePasswordView(rest_framework.views.APIView):
    http_method_names = ('post',)
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    def post(self, request):
        if not django.contrib.auth.hashers.check_password(
            request.data.get('oldPassword'),
            request.user.password,
        ):
            return rest_framework.response.Response(
                {'reason': 'Указанный пароль не совпадает с действительным.'},
                status=rest_framework.status.HTTP_403_FORBIDDEN,
            )

        serializer = api.me.serializers.PasswordSerializer(
            request.user,
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()
            return rest_framework.response.Response(
                {'status': 'ok'},
                status=rest_framework.status.HTTP_200_OK,
            )

        return api.utils.get_error_response(serializer)
