# Generated by Django 3.0 on 2020-01-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_auto_20191219_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodereview',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
