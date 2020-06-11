# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20180330_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='order_by_integer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
