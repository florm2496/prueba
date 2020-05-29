# Generated by Django 3.0.6 on 2020-05-18 14:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0003_auto_20200516_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avisos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', ckeditor.fields.RichTextField()),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'aviso',
                'verbose_name_plural': 'avisos',
            },
        ),
    ]