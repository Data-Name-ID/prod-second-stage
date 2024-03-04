import django.contrib.auth.hashers
import rest_framework.serializers

import api.users.models
import api.utils


class UserSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = api.users.models.User
        exclude = ('id',)
        extra_kwargs = {  # noqa: RUF012
            'password': {
                'error_messages': {
                    'required': 'Поле пароля является обязательным.',
                    'null': 'Поле пароля не может быть пустым.',
                },
                'write_only': True,
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

    def create(self, validated_data):
        validated_data['password'] = django.contrib.auth.hashers.make_password(
            validated_data['password'],
        )
        return super().create(validated_data)

    def validate(self, data):
        if not api.utils.check_country_code(
            data.get('countryCode'),
        ):
            msg = 'Некорректный код страны.'
            raise rest_framework.serializers.ValidationError(msg)

        return super().validate(data)
