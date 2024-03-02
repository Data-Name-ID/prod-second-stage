import rest_framework.serializers

import api.posts.models


class PostSerializer(rest_framework.serializers.ModelSerializer):
    tags = rest_framework.serializers.SerializerMethodField()

    class Meta:
        model = api.posts.models.Post
        fields = ('id', 'content', 'author', 'createdAt', 'tags')
        read_only_fields = ('id', 'author', 'createdAt', 'tags')
        depth = 1

    def get_tags(self, instance):
        return [tag.name for tag in instance.tags.all()]

    def create(self, validated_data):
        return api.posts.models.Post.objects.create(
            **validated_data,
            author=self.context['request'].user,
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.login
        return representation
