# Generated by Django 5.0.7 on 2024-08-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_ingredient_measure_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
