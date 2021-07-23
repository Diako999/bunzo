# Generated by Django 3.2.5 on 2021-07-19 15:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('tag', models.CharField(max_length=150)),
                ('published_date', models.DateTimeField(default=datetime.datetime(2021, 7, 19, 15, 40, 29, 138715, tzinfo=utc))),
                ('reading_time', models.IntegerField(blank=True)),
                ('likes', models.IntegerField(blank=True)),
                ('comments', models.IntegerField(blank=True)),
                ('post_detail', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]