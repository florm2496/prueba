# Generated by Django 3.0.7 on 2020-07-21 22:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('emergencias', '0012_auto_20200721_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencia',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2020, 7, 21, 22, 29, 54, 654433, tzinfo=utc)),
        ),
    ]