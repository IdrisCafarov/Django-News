# Generated by Django 4.1 on 2022-08-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_category_created_date_category_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=25, verbose_name='Category title'),
        ),
    ]