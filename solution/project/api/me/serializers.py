import django.contrib.auth.hashers
import django.core.validators
import rest_framework.serializers

import api.users.models
import api.utils


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
