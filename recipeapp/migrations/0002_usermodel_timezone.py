# Generated by Django 3.2.6 on 2021-09-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='timezone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
