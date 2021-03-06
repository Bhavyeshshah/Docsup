# Generated by Django 3.2.6 on 2021-10-12 09:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesandingredients', '0028_alter_nutritiondetails_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritiondetails',
            name='weight',
            field=models.CharField(max_length=225, validators=[django.core.validators.RegexValidator(message='exmaple of valid weight be 240g or 240kg or 240lb', regex='\\d{1,9}(kg|lb)')]),
        ),
    ]
