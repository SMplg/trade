# Generated by Django 3.2.9 on 2022-04-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_mainpage_actual_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='actual_products',
            field=models.ManyToManyField(to='mainapp.Product', verbose_name='Актуальные'),
        ),
    ]