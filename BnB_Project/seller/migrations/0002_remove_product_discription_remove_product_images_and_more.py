# Generated by Django 5.0.2 on 2024-02-17 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Discription',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Images',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Visible',
        ),
    ]
