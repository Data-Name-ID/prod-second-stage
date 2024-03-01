import django.core.validators
import django.db.models


class Country(django.db.models.Model):
    name = django.db.models.CharField('Название', max_length=100)
    alpha2 = django.db.models.CharField(
        'Двухбуквенный код страны',
        max_length=2,
        validators=[
            django.core.validators.RegexValidator(
                regex=r'[a-zA-Z]{2}',
                message='Двухбуквенный код страны должен состоять из 2 букв.',
            ),
        ],
    )
    alpha3 = django.db.models.CharField(
        'Трёхбуквенный код страны',
        max_length=3,
        validators=[
            django.core.validators.RegexValidator(
                regex=r'[a-zA-Z]{3}',
                message='Трёхбуквенный код страны должен состоять из 3 букв.',
            ),
        ],
    )
    region = django.db.models.TextField(
        'Географический регион',
        validators=[
            django.core.validators.RegexValidator(
                regex=r'^(Europe|Africa|Americas|Oceania|Asia)$',
                message=(
                    'Географический регион должен быть Europe, '
                    'Africa, Americas, Oceania или Asia.'
                ),
            ),
        ],
    )

    class Meta:
        db_table = 'countries'
        ordering = ('alpha2',)
        managed = False

    def __str__(self):
        return self.name
