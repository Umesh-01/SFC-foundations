# Generated by Django 3.2 on 2021-05-12 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20210512_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='source',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
