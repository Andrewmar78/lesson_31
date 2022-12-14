# Generated by Django 4.1.1 on 2022-09-13 16:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_ad_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(5, 'The field must contain at least 5 characters')]),
        ),
    ]
