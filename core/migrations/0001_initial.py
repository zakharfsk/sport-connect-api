# Generated by Django 5.0 on 2024-06-15 14:35

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225, verbose_name='Вид спорту')),
            ],
            options={
                'verbose_name': 'Вид спорту',
                'verbose_name_plural': 'Види спорту',
                'db_table': 'sports',
            },
        ),
        migrations.CreateModel(
            name='SportStandard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('Зріст, см', 'Зріст, см'), ('Ваго-ростовий індекс (індекс маси тіла)', 'Ваго-ростовий індекс (індекс маси тіла)'), ('Індекс розвитку мускулатури (периметр плеча напруженого/периметр плеча розслабленого)', 'Індекс розвитку мускулатури (периметр плеча напруженого/периметр плеча розслабленого)'), ('Співвідношення розмаху рук до довжини тіла стоячи, см', 'Співвідношення розмаху рук до довжини тіла стоячи, см'), ('Біг 30м, с', 'Біг 30м, с'), ('Стрибок з місця у довжину, см', 'Стрибок з місця у довжину, см'), ('Кидок набивного м’яча на дальність (1 кг), м', 'Кидок набивного м’яча на дальність (1 кг), м'), ('Підіймання тулуба в сід за 60с, кількість', 'Підіймання тулуба в сід за 60с, кількість'), ('Згинання розгинання рук в упорі лежачи, кількість', 'Згинання розгинання рук в упорі лежачи, кількість'), ('Нахил тулуба стоячи (нахили тулуба вперед з положення сидячи), см', 'Нахил тулуба стоячи (нахили тулуба вперед з положення сидячи), см'), ('Човниковий біг (4х9м), с', 'Човниковий біг (4х9м), с'), ('Швидкість реакції (ловля палиця, яка має сантиметрові помітки), см', 'Швидкість реакції (ловля палиця, яка має сантиметрові помітки), см'), ('Стрибки на скакалці за 60с, кількість', 'Стрибки на скакалці за 60с, кількість'), ('Викрут мірної лінійки (різниця від ширини плечей), см', 'Викрут мірної лінійки (різниця від ширини плечей), см')], max_length=225, unique=True, verbose_name='Назва стандарту')),
            ],
            options={
                'verbose_name': 'Стандарт',
                'verbose_name_plural': 'Стандарти',
            },
        ),
        migrations.CreateModel(
            name='SportSchool',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=350, verbose_name='Назва ДЮСШ')),
                ('school_site_url', models.URLField(verbose_name='Сайт ДЮСШ')),
                ('school_sport_address', models.CharField(max_length=350, verbose_name='Адреса ДЮСШ')),
                ('school_sport_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Електронна адреса ДЮСШ')),
                ('school_sport_phone_numbers', models.CharField(blank=True, max_length=500, null=True, verbose_name='Телефони ДЮСШ')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sport_schools', to='core.sport', verbose_name='Вид спорту')),
            ],
            options={
                'verbose_name': 'Сайт ДЮСШ',
                'verbose_name_plural': 'Сайти ДЮСШ',
                'db_table': 'sport_school',
            },
        ),
        migrations.CreateModel(
            name='AverageValuesStandards',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('children_age', models.IntegerField(choices=[(10, 10), (11, 11)], null=True, verbose_name='Вік дитини')),
                ('children_gender', models.CharField(choices=[('Юнак', 'Юнак'), ('Дівчина', 'Дівчина')], max_length=225, null=True, verbose_name='Стать дитини')),
                ('average_value', models.FloatField(null=True, verbose_name='Середнє значення')),
                ('sigma', models.FloatField(verbose_name='Сигма')),
                ('name_standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sportstandard', verbose_name='Показник')),
            ],
            options={
                'verbose_name': 'Середні значення по нормативах',
                'verbose_name_plural': 'Середні значення по нормативах',
                'db_table': 'average_values_standards',
            },
        ),
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('result', models.JSONField(verbose_name='Результат')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_results', to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результати',
            },
        ),
        migrations.CreateModel(
            name='WeightingFactors',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('weighting_factor', models.FloatField(verbose_name='Ваговий коефіцієнт')),
                ('average_value_standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weighting_factors', to='core.averagevaluesstandards', verbose_name='Норматив')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weighting_factors', to='core.sport', verbose_name='Вид спорту')),
            ],
            options={
                'verbose_name': 'Вагові коефіцієнти (за випробуваннями)',
                'verbose_name_plural': 'Вагові коефіцієнти (за випробуваннями)',
                'db_table': 'weighting_factors',
            },
        ),
    ]
