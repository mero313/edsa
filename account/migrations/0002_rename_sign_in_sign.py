# Generated by Django 4.1.5 on 2023-03-01 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sign_in',
            new_name='sign',
        ),
    ]
