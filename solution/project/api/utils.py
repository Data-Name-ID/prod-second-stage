import rest_framework.response
import rest_framework.status

import api.countries.models


def get_profile_response(request):
    data = {
        'login': request.user.login,
        'email': request.user.email,
        'countryCode': request.user.countryCode,
        'isPublic': request.user.isPublic,
    }

    if request.user.phone:
        data['phone'] = request.user.phone
    if request.user.image:
        data['image'] = request.user.image

    return rest_framework.response.Response(
        data,
        status=rest_framework.status.HTTP_200_OK,
    )


def get_error_response(
    serializer,
    error_status=rest_framework.status.HTTP_400_BAD_REQUEST,
):
    return rest_framework.response.Response(
        {'reason': next(iter(serializer.errors.values()))},
        status=error_status,
    )


def check_country_code(country_code):
    if not country_code:
        return True

    if api.countries.models.Country.objects.filter(
        alpha2=country_code,
    ).exists():
        return True

    return False
