# Generated by Django 3.2.6 on 2021-09-30 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesandingredients', '0019_auto_20210928_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=225)),
                ('company_name', models.CharField(max_length=225)),
                ('category', models.CharField(max_length=225)),
            ],
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='category',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
