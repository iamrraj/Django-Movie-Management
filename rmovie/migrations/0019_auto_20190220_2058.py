# Generated by Django 2.0.4 on 2019-02-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmovie', '0018_auto_20190220_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviee',
            name='description',
            field=models.TextField(),
        ),
    ]
