# Generated by Django 3.0.5 on 2020-05-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge', '0005_bridge_year_built'),
    ]

    operations = [
        migrations.AddField(
            model_name='bridge',
            name='lat',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='bridge',
            name='long',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
