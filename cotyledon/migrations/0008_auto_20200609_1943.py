# Generated by Django 3.0.7 on 2020-06-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotyledon', '0007_plant_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='count',
        ),
        migrations.AddField(
            model_name='event',
            name='count',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
