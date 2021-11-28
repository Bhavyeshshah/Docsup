# Generated by Django 3.2.6 on 2021-10-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesandingredients', '0035_ingredientsuppliers_preferred'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_image', models.ImageField(blank=True, upload_to='recipeimages')),
            ],
        ),
        migrations.AddField(
            model_name='recipesmodel',
            name='recipe_images',
            field=models.ManyToManyField(blank=True, to='recipesandingredients.RecipeImages'),
        ),
    ]
