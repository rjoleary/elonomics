# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elonomics', '0003_auto_20150323_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='outcome',
            field=models.CharField(choices=[('CM', 'checkmates'), ('SM', 'stalemates')], default='CM', max_length=2),
            preserve_default=True,
        ),
    ]
