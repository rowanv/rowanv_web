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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=600)),
                ('current_project', models.BooleanField(default=False)),
                ('date_undertaken', models.DateField(default=django.utils.timezone.now)),
                ('link', models.CharField(max_length=200, default='https://www.linkedin.com/in/rowanv')),
                ('thumbnail', models.ImageField(upload_to='', default='http://placehold.it/700x300')),
                ('tag_name', models.CharField(max_length=100)),
                ('code_link', models.CharField(null=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='skills_list',
            field=models.ManyToManyField(to='portfolio.Skill'),
        ),
    ]
