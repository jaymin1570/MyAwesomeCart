# Generated by Django 3.0 on 2020-04-18 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orderupdate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]