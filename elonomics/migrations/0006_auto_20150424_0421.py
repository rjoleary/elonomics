# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elonomics', '0005_auto_20150424_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='outcome',
            field=models.IntegerField(max_length=2, default=1, choices=[(1, 'checkmates'), (2, 'stalemates'), (3, 'draws'), (4, 'bribes')]),
            preserve_default=True,
        ),
    ]
