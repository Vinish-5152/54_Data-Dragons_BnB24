# Generated by Django 5.0.2 on 2024-02-17 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_rename_category_product_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='Quantity',
        ),
    ]
