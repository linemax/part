# Generated by Django 3.2 on 2021-10-06 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='OrderModel',
        ),
    ]