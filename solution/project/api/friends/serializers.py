import rest_framework.serializers

import api.friends.models


class FriendsSerializer(rest_framework.serializers.ModelSerializer):
    login = rest_framework.serializers.CharField(source='to_user')
    addedAt = rest_framework.serializers.DateTimeField(source='created_at')

    class Meta:
        model = api.friends.models.Friendship
        fields = ('login', 'addedAt')
