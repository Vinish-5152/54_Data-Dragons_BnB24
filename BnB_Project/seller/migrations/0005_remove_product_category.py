# Generated by Django 5.0.2 on 2024-02-17 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_rename_category_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
    ]
