# Generated by Django 3.2.6 on 2021-09-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesandingredients', '0003_alter_ingredients_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='qtyUnits',
            field=models.CharField(blank=True, choices=[('-- Weight --', (('19', 'Ounce (oz) (28.35 g)'), ('18', 'Pound (lb) (453.59 g)'), ('9', 'Kilogram (Kg) (1000 g)'), ('6', 'Tonne (T) (1000000 g)'))), ('-- Volume --', (('25', 'Pinch (pinch) (0.3 ml)'), ('22', 'US Teaspoon (tsp) (4.93 ml)'), ('21', 'US Tablespoon (tbsp) (14.79 ml)'), ('17', 'Fluid-ounce (floz) (29.57 ml)'), ('11', 'Deciliter (dL) (100 ml)'), ('20', 'US Cup (cup) (236.59 ml)'), ('16', 'Pint (pt) (473.18 ml)')))], max_length=225, null=True),
        ),
    ]