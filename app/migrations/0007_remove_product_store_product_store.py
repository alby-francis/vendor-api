# Generated by Django 4.2.11 on 2024-03-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_product_unit_sold_alter_product_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='store',
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ManyToManyField(related_name='products', to='app.store'),
        ),
    ]
