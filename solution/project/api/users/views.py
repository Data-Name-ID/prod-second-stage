import rest_framework.generics
import rest_framework.response
import rest_framework.status

import api.users.models
import api.users.serializers


class RegisterView(rest_framework.generics.CreateAPIView):
    http_method_names = ('post',)

    serializer_class = api.users.serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if (
                api.users.models.User.objects.filter(
                    email=request.data['email'],
                ).exists()
                or api.users.models.User.objects.filter(
                    phone=request.data['phone'],
                ).exists()
                or api.users.models.User.objects.filter(
                    login=request.data['login'],
                ).exists()
            ):
                return rest_framework.response.Response(
                    {
                        'reason': (
                            'Пользователь с таким email, телефоном или '
                            'логином уже зарегистрирован.'
                        ),
                    },
                    status=rest_framework.status.HTTP_409_CONFLICT,
                )

            serializer.save()

            user_profile = {
                'login': serializer.data.get('login'),
                'email': serializer.data.get('email'),
                'countryCode': serializer.data.get('countryCode'),
                'isPublic': serializer.data.get('isPublic'),
            }

            if serializer.data.get('phone'):
                user_profile['phone'] = serializer.data.get('phone')
            if serializer.data.get('image'):
                user_profile['image'] = serializer.data.get('image')

            return rest_framework.response.Response(
                {'profile': user_profile},
                status=rest_framework.status.HTTP_201_CREATED,
            )

        return rest_framework.response.Response(
            {'reason': next(iter(serializer.errors.values()))},
            status=rest_framework.status.HTTP_400_BAD_REQUEST,
        )
