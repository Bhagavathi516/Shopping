# Generated by Django 3.2.12 on 2023-08-11 10:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0013_alter_shoppingitemmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitemmodel',
            name='discount',
            field=models.FloatField(blank=True, default=0.0, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
