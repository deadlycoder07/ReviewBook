# Generated by Django 3.0 on 2020-01-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20200121_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamereview',
            name='body',
            field=models.CharField(max_length=500),
        ),
    ]
