# Generated by Django 3.0.6 on 2020-05-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0005_auto_20200518_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avisos',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
