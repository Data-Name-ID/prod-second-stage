import rest_framework.decorators
import rest_framework.response
import rest_framework.status
import rest_framework.viewsets

import api.countries.models
import api.countries.serializers


class CountriesViewSet(rest_framework.viewsets.ModelViewSet):
    http_method_names = ('get',)

    queryset = api.countries.models.Country.objects.all()
    serializer_class = api.countries.serializers.CountrySerializer
    filterset_fields = ('region',)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @rest_framework.decorators.action(
        detail=False,
        url_path=r'(?P<alpha2>[A-Za-z]{2})',
    )
    def get_country_by_alpha2(self, request, alpha2):
        try:
            country = self.queryset.get(alpha2=alpha2)
        except api.countries.models.Country.DoesNotExist:
            return rest_framework.response.Response(
                {'reason': 'Страна с указанным кодом не найдена.'},
                status=rest_framework.status.HTTP_404_NOT_FOUND,
            )

        serializer = self.get_serializer(country)
        return rest_framework.response.Response(
            serializer.data,
            status=rest_framework.status.HTTP_200_OK,
        )
