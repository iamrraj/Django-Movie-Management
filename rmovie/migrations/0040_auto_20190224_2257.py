# Generated by Django 2.0.4 on 2019-02-24 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rmovie', '0039_auto_20190224_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='rmovie.Moviee'),
        ),
    ]
