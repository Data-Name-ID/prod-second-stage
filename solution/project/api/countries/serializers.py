import rest_framework.serializers

import api.countries.models


class CountrySerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = api.countries.models.Country
        exclude = ('id',)
