import django.contrib.auth.hashers
import django.core.validators
import django.db.models


class User(django.db.models.Model):
    login = django.db.models.CharField(
        'Логин',
        max_length=30,
        validators=[
            django.core.validators.RegexValidator(
                regex=r'[a-zA-Z0-9-]+',
                message=(
                    'Логин должен состоять только из '
                    'латинских букв, цифр и дефисов.'
                ),
            ),
        ],
    )
    email = django.db.models.CharField('Электронная почта', max_length=50)
    password = django.db.models.CharField(
        'Пароль',
        validators=[
            django.core.validators.RegexValidator(
                regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,100}$',
                message=(
                    'Пароль должен содержать минимум 6 символов, '
                    'одну заглавную букву, одну строчную букву и одну цифру.'
                ),
            ),
        ],
    )
    countryCode = django.db.models.CharField(
        'Код страны',
        max_length=2,
        validators=[
            django.core.validators.RegexValidator(
                regex=r'[a-zA-Z]{2}',
                message='Код страны должен состоять из 2 букв.',
            ),
        ],
    )
    isPublic = django.db.models.BooleanField('Публичный профиль')
    phone = django.db.models.CharField(
        'Номер телефона',
        max_length=20,
        validators=[
            django.core.validators.RegexValidator(
                regex=r'\+[\d]+',
                message=(
                    'Номер телефона должен начинаться с + и '
                    'состоять только из цифр.'
                ),
            ),
        ],
        default='',
    )
    image = django.db.models.CharField(
        'URL изображения',
        max_length=200,
        default='',
    )

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.login

    def is_authenticated(self):
        return True
