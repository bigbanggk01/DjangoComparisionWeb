# Generated by Django 3.2.7 on 2021-11-05 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_categort_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=1000, null=True),
        ),
    ]
