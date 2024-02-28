import django.core.validators
import django.db.models


class Country(django.db.models.Model):
    name = django.db.models.CharField(max_length=100)
    alpha2 = django.db.models.CharField(
        max_length=2,
        validators=[
            django.core.validators.RegexValidator(
                regex=r'[a-zA-Z]{2}',
            ),
        ],
    )
    alpha3 = django.db.models.CharField(
        max_length=3,
        validators=[
            django.core.validators.RegexValidator(
                regex=r'[a-zA-Z]{3}',
            ),
        ],
    )
    region = django.db.models.TextField()

    class Meta:
        db_table = 'countries'
        ordering = ('alpha2',)

    def __str__(self):
        return self.name
