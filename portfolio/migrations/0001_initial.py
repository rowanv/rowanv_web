# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('current_project', models.BooleanField(default=False)),
                ('date_undertaken', models.DateField(default=django.utils.timezone.now)),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
    ]
