import django.conf
import jwt
import rest_framework.authentication
import rest_framework.exceptions

import api.users.models


class TokenAuthentication(rest_framework.authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')

        if not token:
            return None

        if not token.startswith('Bearer '):
            raise rest_framework.exceptions.NotAuthenticated

        try:
            payload = jwt.decode(
                token[7:],
                django.conf.settings.SECRET_KEY,
                algorithms='HS256',
            )

            user = api.users.models.User.objects.get(login=payload['login'])

            if payload['password'] != user.password:
                raise rest_framework.exceptions.NotAuthenticated
        except (
            api.users.models.User.DoesNotExist,
            jwt.exceptions.PyJWTError,
        ) as e:
            raise rest_framework.exceptions.NotAuthenticated from e

        return (user, None)
