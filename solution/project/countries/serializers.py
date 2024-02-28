import rest_framework.serializers

import countries.models


class CountrySerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = countries.models.Country
        fields = ('name', 'alpha2', 'alpha3', 'region')
