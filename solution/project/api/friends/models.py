import django.db.models

import api.users.models


class Friendship(django.db.models.Model):
    from_user = django.db.models.ForeignKey(
        api.users.models.User,
        related_name='friendship_from',
        on_delete=django.db.models.CASCADE,
    )
    to_user = django.db.models.ForeignKey(
        api.users.models.User,
        related_name='friendship_to',
        on_delete=django.db.models.CASCADE,
    )
    created_at = django.db.models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'friendships'
        unique_together = (
            'from_user',
            'to_user',
        )
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.from_user} -> {self.to_user}'
