import django.contrib.auth.hashers
import rest_framework.serializers

import api.users.models


class UserSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = api.users.models.User
        fields = '__all__'
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

    def create(self, validated_data):
        validated_data['password'] = django.contrib.auth.hashers.make_password(
            validated_data['password'],
        )
        return super().create(validated_data)