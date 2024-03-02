import rest_framework.exceptions
import rest_framework.response
import rest_framework.views


def exception_handler(exc, context):
    if isinstance(exc, rest_framework.exceptions.NotAuthenticated):
        return rest_framework.response.Response(
            {'reason': 'Переданный токен не существует либо некорректен.'},
            status=401,
        )

    return rest_framework.views.exception_handler(exc, context)
