# Generated by Django 2.0.4 on 2019-02-20 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rmovie', '0015_moviee_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='rmovie.Moviee'),
        ),
    ]