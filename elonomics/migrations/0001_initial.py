# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('time_played', models.DateTimeField()),
                ('story', models.CharField(help_text='Use the format: In a long and adventurous battle...', max_length=100)),
                ('player1_before_game_elo', models.IntegerField()),
                ('player2_before_game_elo', models.IntegerField()),
                ('outcome', models.IntegerField(choices=[(1, 'checkmates'), (2, 'stalemates'), (3, 'draws'), (4, 'bribes')], max_length=2, default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('user_name', models.SlugField(max_length=30, unique=True)),
                ('full_name', models.CharField(max_length=30)),
                ('sign_off', models.CharField(max_length=10)),
                ('elo_score', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='player1',
            field=models.ForeignKey(to='elonomics.Player', related_name='player1'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='player2',
            field=models.ForeignKey(to='elonomics.Player', related_name='player2'),
            preserve_default=True,
        ),
    ]
