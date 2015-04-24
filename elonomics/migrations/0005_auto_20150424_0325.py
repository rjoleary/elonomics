# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elonomics', '0004_game_outcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='outcome',
            field=models.CharField(max_length=2, choices=[(1, 'checkmates'), (2, 'stalemates'), (3, 'draws'), (4, 'bribes')], default=1),
            preserve_default=True,
        ),
    ]
