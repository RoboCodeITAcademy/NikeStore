# Generated by Django 3.2.4 on 2021-07-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_other_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='other_colors',
            field=models.ManyToManyField(related_name='other_colors', to='shop.Colors'),
        ),
    ]
