# Generated by Django 5.1 on 2024-08-31 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='products.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=1, verbose_name='Размер'),
        ),
    ]
