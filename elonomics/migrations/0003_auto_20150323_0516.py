# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elonomics', '0002_auto_20150323_0458'),
    ]

    operations = [
            migrations.RemoveField('Game', 'outcome'),
            migrations.DeleteModel('Outcome')
    ]
