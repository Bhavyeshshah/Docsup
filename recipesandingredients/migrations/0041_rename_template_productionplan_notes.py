# Generated by Django 3.2.6 on 2021-11-05 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipesandingredients', '0040_rename_date_filed_productionplan_date_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productionplan',
            old_name='template',
            new_name='notes',
        ),
    ]
