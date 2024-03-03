import rest_framework.serializers

import api.posts.models


class PostSerializer(rest_framework.serializers.ModelSerializer):
    tags = rest_framework.serializers.SerializerMethodField()
    author = rest_framework.serializers.SerializerMethodField()
    likesCount = rest_framework.serializers.SerializerMethodField(
        'get_likes_count',
    )
    dislikesCount = rest_framework.serializers.SerializerMethodField(
        'get_dislikes_count',
    )

    class Meta:
        model = api.posts.models.Post
        fields = (
            'id',
            'content',
            'author',
            'createdAt',
            'tags',
            'likesCount',
            'dislikesCount',
        )
        read_only_fields = (
            'id',
            'author',
            'createdAt',
            'likesCount',
            'dislikesCount',
        )

    def create(self, validated_data):
        return api.posts.models.Post.objects.create(
            **validated_data,
            author=self.context['request'].user,
        )

    def get_tags(self, instance):
        return [tag.name for tag in instance.tags.all()]

    def get_author(self, instance):
        return instance.author.login

    def get_likes_count(self, instance):
        return instance.likes.count()

    def get_dislikes_count(self, instance):
        return instance.dislikes.count()
