import django.contrib.auth.hashers
import django.core.validators
import rest_framework.serializers

import api.users.models
import api.users.serializers
import api.utils


class UserSerializer(api.users.serializers.UserSerializer):
    class Meta:
        model = api.users.models.User
        fields = ('phone', 'countryCode', 'isPublic', 'image')
        extra_kwargs = {  # noqa: RUF012
            'password': {
                'error_messages': {
                    'required': 'Поле пароля является обязательным.',
                    'null': 'Поле пароля не может быть пустым.',
                },
            },
            'email': {
                'error_messages': {
                    'required': (
                        'Поле электронной почты является обязательным.'
                    ),
                    'null': 'Поле электронной почты не может быть пустым.',
                },
            },
            'login': {
                'error_messages': {
                    'required': 'Поле логина является обязательным.',
                    'null': 'Поле логина не может быть пустым.',
                },
            },
            'countryCode': {
                'error_messages': {
                    'required': 'Поле кода страны является обязательным.',
                    'null': 'Поле кода страны не может быть пустым.',
                },
            },
            'isPublic': {
                'error_messages': {
                    'required': 'Поле публичности является обязательным.',
                    'null': 'Поле публичности не может быть пустым.',
                },
            },
        }


class PasswordSerializer(rest_framework.serializers.ModelSerializer):
    oldPassword = rest_framework.serializers.CharField()
    newPassword = rest_framework.serializers.CharField(
        source='password',
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

    class Meta:
        model = api.users.models.User
        fields = ('oldPassword', 'newPassword')

    def update(self, instance, validated_data):
        validated_data['password'] = django.contrib.auth.hashers.make_password(
            validated_data['password'],
        )
        return super().update(instance, validated_data)

    def validate(self, data):
        if not api.utils.check_country_code(
            data.get('countryCode'),
        ):
            msg = 'Некорректный код страны.'
            raise rest_framework.serializers.ValidationError(msg)

        return super().validate(data)
