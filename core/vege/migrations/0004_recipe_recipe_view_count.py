# Generated by Django 4.2.4 on 2023-08-21 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
