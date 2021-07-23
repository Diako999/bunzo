# Generated by Django 3.2.5 on 2021-07-19 15:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 19, 15, 52, 46, 246664, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='reading_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]