# Generated by Django 3.0 on 2020-02-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20200201_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
