# Generated by Django 2.0.4 on 2019-02-14 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rmovie', '0010_auto_20190214_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rmovie.Moviee'),
        ),
        migrations.AlterField(
            model_name='detai',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rmovie.Moviee'),
        ),
    ]
