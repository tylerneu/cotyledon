# Generated by Django 3.0.7 on 2020-06-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotyledon', '0004_auto_20200609_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]
