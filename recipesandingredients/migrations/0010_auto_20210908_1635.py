# Generated by Django 3.2.6 on 2021-09-08 11:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesandingredients', '0009_alter_ingredients_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredients',
            old_name='fromMeasurement',
            new_name='toMeasurementData',
        ),
        migrations.RenameField(
            model_name='ingredients',
            old_name='toMeasurement',
            new_name='toMeasurementUnits',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='fromMeasurementData',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=225), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='fromMeasurementUnits',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=225), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='parUnits',
            field=models.CharField(blank=True, choices=[('-- Weight --', (('Ounce (oz) (28.35 g)', 'Ounce (oz) (28.35 g)'), ('Pound (lb) (453.59 g)', 'Pound (lb) (453.59 g)'), ('Kilogram (Kg) (1000 g)', 'Kilogram (Kg) (1000 g)'), ('Tonne (T) (1000000 g)', 'Tonne (T) (1000000 g)'))), ('-- Volume --', (('Pinch (pinch) (0.3 ml)', 'Pinch (pinch) (0.3 ml)'), ('US Teaspoon (tsp) (4.93 ml)', 'US Teaspoon (tsp) (4.93 ml)'), ('US Tablespoon (tbsp) (14.79 ml)', 'US Tablespoon (tbsp) (14.79 ml)'), ('Fluid-ounce (floz) (29.57 ml)', 'Fluid-ounce (floz) (29.57 ml)'), ('Deciliter (dL) (100 ml)', 'Deciliter (dL) (100 ml)'), ('US Cup (cup) (236.59 ml)', 'US Cup (cup) (236.59 ml)'), ('Pint (pt) (473.18 ml)', 'Pint (pt) (473.18 ml)'))), ('-- Quantity --', (('Dozen (dozen) (12 each)', 'Dozen (dozen) (12 each)'), ('Hundred (hundred) (100 each)', 'Hundred (hundred) (100 each)'), ('Thousand (thousand) (1000 each)', 'Thousand (thousand) (1000 each)'), ('Million (million) (1000000 each)', 'Million (million) (1000000 each)'))), ('-- Time --', (('Second (s)', 'Second (s)'), ('Minute (min) (60 s)', 'Minute (min) (60 s)'), ('Hour (hr) (3600 s)', 'Hour (hr) (3600 s)')))], max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='qtyUnits',
            field=models.CharField(blank=True, choices=[('-- Weight --', (('Ounce (oz) (28.35 g)', 'Ounce (oz) (28.35 g)'), ('Pound (lb) (453.59 g)', 'Pound (lb) (453.59 g)'), ('Kilogram (Kg) (1000 g)', 'Kilogram (Kg) (1000 g)'), ('Tonne (T) (1000000 g)', 'Tonne (T) (1000000 g)'))), ('-- Volume --', (('Pinch (pinch) (0.3 ml)', 'Pinch (pinch) (0.3 ml)'), ('US Teaspoon (tsp) (4.93 ml)', 'US Teaspoon (tsp) (4.93 ml)'), ('US Tablespoon (tbsp) (14.79 ml)', 'US Tablespoon (tbsp) (14.79 ml)'), ('Fluid-ounce (floz) (29.57 ml)', 'Fluid-ounce (floz) (29.57 ml)'), ('Deciliter (dL) (100 ml)', 'Deciliter (dL) (100 ml)'), ('US Cup (cup) (236.59 ml)', 'US Cup (cup) (236.59 ml)'), ('Pint (pt) (473.18 ml)', 'Pint (pt) (473.18 ml)'))), ('-- Quantity --', (('Dozen (dozen) (12 each)', 'Dozen (dozen) (12 each)'), ('Hundred (hundred) (100 each)', 'Hundred (hundred) (100 each)'), ('Thousand (thousand) (1000 each)', 'Thousand (thousand) (1000 each)'), ('Million (million) (1000000 each)', 'Million (million) (1000000 each)'))), ('-- Time --', (('Second (s)', 'Second (s)'), ('Minute (min) (60 s)', 'Minute (min) (60 s)'), ('Hour (hr) (3600 s)', 'Hour (hr) (3600 s)')))], max_length=225, null=True),
        ),
    ]
