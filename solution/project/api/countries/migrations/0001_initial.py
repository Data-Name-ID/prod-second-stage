# Generated by Django 4.2.10 on 2024-03-03 14:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('alpha2', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(message='Двухбуквенный код страны должен состоять из 2 букв.', regex='[a-zA-Z]{2}')], verbose_name='Двухбуквенный код страны')),
                ('alpha3', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(message='Трёхбуквенный код страны должен состоять из 3 букв.', regex='[a-zA-Z]{3}')], verbose_name='Трёхбуквенный код страны')),
                ('region', models.TextField(validators=[django.core.validators.RegexValidator(message='Географический регион должен быть Europe, Africa, Americas, Oceania или Asia.', regex='^(Europe|Africa|Americas|Oceania|Asia)$')], verbose_name='Географический регион')),
            ],
            options={
                'db_table': 'countries',
                'ordering': ('alpha2',),
                'managed': False,
            },
        ),
    ]
