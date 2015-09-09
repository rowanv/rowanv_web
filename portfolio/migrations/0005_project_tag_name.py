# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20150909_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tag_name',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
