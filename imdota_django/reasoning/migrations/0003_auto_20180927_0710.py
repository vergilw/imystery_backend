# Generated by Django 2.1.1 on 2018-09-27 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reasoning', '0002_auto_20180927_0343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='grade',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='studio',
            old_name='grade',
            new_name='score',
        ),
    ]