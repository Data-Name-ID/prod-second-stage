import django.core.exceptions
import django.http.response
import rest_framework.exceptions
import rest_framework.response
import rest_framework.views


def exception_handler(exc, context):
    if isinstance(exc, rest_framework.exceptions.NotAuthenticated):
        return rest_framework.response.Response(
            {'reason': 'Переданный токен не существует либо некорректен.'},
            status=401,
        )

    if isinstance(exc, django.http.response.Http404):
        exc = rest_framework.exceptions.NotFound()
    elif isinstance(exc, django.core.exceptions.PermissionDenied):
        exc = rest_framework.exceptions.PermissionDenied()

    if isinstance(exc.detail, dict):
        exc.detail = {'reason': next(iter(exc.detail.values()))}
    elif isinstance(exc.detail, list):
        exc.detail = {'reason': exc.detail[0]}
    else:
        exc.detail = {'reason': exc.detail}

    return rest_framework.views.exception_handler(exc, context)
