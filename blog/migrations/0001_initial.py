# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-09-04 14:14
from __future__ import unicode_literals

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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateField(default=datetime.datetime(2018, 9, 4, 14, 14, 19, 430693, tzinfo=utc))),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateField(default=datetime.datetime(2018, 9, 4, 14, 14, 19, 430113, tzinfo=utc))),
                ('published_date', models.DateField(blank=True, null=True)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='blog.Post'),
        ),
    ]
