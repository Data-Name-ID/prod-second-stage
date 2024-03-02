import uuid

import django.db.models

import api.users.models


class Tag(django.db.models.Model):
    name = django.db.models.CharField(max_length=30)

    class Meta:
        db_table = 'tags'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(django.db.models.Model):
    id = django.db.models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = django.db.models.TextField(max_length=1000)
    author = django.db.models.ForeignKey(
        api.users.models.User,
        on_delete=django.db.models.CASCADE,
        related_name='posts',
    )
    tags = django.db.models.ManyToManyField(
        Tag,
        related_name='posts',
    )
    createdAt = django.db.models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'
        ordering = ('-createdAt',)

    def __str__(self):
        return self.content[:50]


class PostLike(django.db.models.Model):
    post = django.db.models.ForeignKey(
        Post,
        on_delete=django.db.models.CASCADE,
        related_name='likes',
    )
    user = django.db.models.ForeignKey(
        api.users.models.User,
        on_delete=django.db.models.CASCADE,
        related_name='likes',
    )

    class Meta:
        db_table = 'post_likes'
        unique_together = (
            'post',
            'user',
        )

    def __str__(self):
        return self.post


class PostDislike(django.db.models.Model):
    post = django.db.models.ForeignKey(
        Post,
        on_delete=django.db.models.CASCADE,
        related_name='dislikes',
    )
    user = django.db.models.ForeignKey(
        api.users.models.User,
        on_delete=django.db.models.CASCADE,
        related_name='dislikes',
    )

    class Meta:
        db_table = 'post_dislikes'
        unique_together = (
            'post',
            'user',
        )

    def __str__(self):
        return self.post
