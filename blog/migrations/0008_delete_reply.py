# Generated by Django 4.1 on 2022-08-23 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reply',
        ),
    ]