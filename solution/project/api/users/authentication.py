import django.conf
import jwt
import rest_framework.authentication
import rest_framework.exceptions

import api.users.models


class TokenAuthentication(rest_framework.authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')

        if not token or not token.startswith('Bearer '):
            return None

        try:
            payload = jwt.decode(
                token[7:],
                django.conf.settings.SECRET_KEY,
                algorithms='HS256',
            )
            user = api.users.models.User.objects.get(login=payload['login'])
        except (
            api.users.models.User.DoesNotExist,
            jwt.exceptions.InvalidSignatureError,
        ) as e:
            raise rest_framework.exceptions.NotAuthenticated from e

        return (user, None)
