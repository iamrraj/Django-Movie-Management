# Generated by Django 2.0.4 on 2019-02-24 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmovie', '0027_moviee_quality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviee',
            name='quality',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]