# Generated by Django 3.2.9 on 2022-02-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.PositiveIntegerField(unique=True, verbose_name='Артикул'),
        ),
    ]