# Generated by Django 3.2.12 on 2023-08-08 14:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_auto_20230808_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
