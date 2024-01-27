# Generated by Django 5.0 on 2024-01-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_averagevaluesstandards_name_standard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='averagevaluesstandards',
            name='name_standard',
            field=models.CharField(choices=[('Зріст, см', 'Зріст, см'), ('Вагової-ростовий індекс (індекс маси тіла)', 'Вагової-ростовий індекс (індекс маси тіла)'), ('Індекс розвитку мускулатури (периметр плеча напруженого/периметр плеча розслабленого)', 'Індекс розвитку мускулатури (периметр плеча напруженого/периметр плеча розслабленого)'), ('Співвідношення розмаху рук до довжини тіла стоячи, см', 'Співвідношення розмаху рук до довжини тіла стоячи, см'), ('Біг 30м, с', 'Біг 30м, с'), ('Стрибок з місця у довжину, см', 'Стрибок з місця у довжину, см'), ('Кидок набивного м’яча на дальність (1 кг), м', 'Кидок набивного м’яча на дальність (1 кг), м'), ('Підіймання тулуба в сід за 60с, кількість', 'Підіймання тулуба в сід за 60с, кількість'), ('Згинання розгинання рук в упорі лежачи, кількість', 'Згинання розгинання рук в упорі лежачи, кількість'), ('Нахил тулуба стоячи (нахили тулуба вперед з положення сидячи), см', 'Нахил тулуба стоячи (нахили тулуба вперед з положення сидячи), см'), ('Човниковий біг (4х9м), с', 'Човниковий біг (4х9м), с'), ('Швидкість реакції (ловля палиця, яка має сантиметрові помітки), см', 'Швидкість реакції (ловля палиця, яка має сантиметрові помітки), см'), ('Стрибки на скакалці за 60с, кількість', 'Стрибки на скакалці за 60с, кількість'), ('Викрут мірної лінійки (різниця від ширини плечей), см', 'Викрут мірної лінійки (різниця від ширини плечей), см')], max_length=225, verbose_name='Показник'),
        ),
    ]
