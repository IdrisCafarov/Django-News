# Generated by Django 4.1 on 2022-08-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created date'),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated date'),
        ),
    ]