# Generated by Django 2.0.4 on 2019-02-20 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rmovie', '0016_auto_20190220_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviee',
            old_name='youtube',
            new_name='ytube',
        ),
    ]