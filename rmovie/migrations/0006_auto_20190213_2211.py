# Generated by Django 2.0.4 on 2019-02-13 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rmovie', '0005_remove_cast_cimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviee',
            old_name='date',
            new_name='mdate',
        ),
    ]
