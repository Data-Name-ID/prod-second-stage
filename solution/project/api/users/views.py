import django.conf
import django.contrib.auth.hashers
import django.utils.timezone
import jwt
import rest_framework.generics
import rest_framework.permissions
import rest_framework.response
import rest_framework.status

import api.users.models
import api.users.serializers
import api.utils


class RegisterView(rest_framework.generics.CreateAPIView):
    http_method_names = ('post',)
    serializer_class = api.users.serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if (
                api.users.models.User.objects.filter(
                    email=request.data.get('email'),
                ).exists()
                or api.users.models.User.objects.filter(
                    phone=request.data.get('phone'),
                ).exists()
                or api.users.models.User.objects.filter(
                    login=request.data.get('login'),
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

        return api.utils.get_error_response(serializer)


class SignInView(rest_framework.views.APIView):
    def post(self, request):
        login = request.data.get('login')
        password = request.data.get('password')

        user = api.users.models.User.objects.filter(
            login=login,
        ).filter()

        if not user or not django.contrib.auth.hashers.check_password(
            password,
            user[0].password,
        ):
            return rest_framework.response.Response(
                {'reason': 'Неверный логин или пароль.'},
                status=rest_framework.status.HTTP_401_UNAUTHORIZED,
            )

        token = jwt.encode(
            {
                'login': login,
                'password': user[0].password,
                'exp': django.utils.timezone.now()
                + django.utils.timezone.timedelta(
                    hours=24,
                ),
            },
            django.conf.settings.SECRET_KEY,
            algorithm='HS256',
        )

        return rest_framework.response.Response(
            {'token': token},
            status=rest_framework.status.HTTP_200_OK,
        )
