# Generated by Django 3.2.7 on 2021-11-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211105_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.TextField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
