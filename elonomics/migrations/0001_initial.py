# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_played', models.DateTimeField()),
                ('story', models.CharField(max_length=100, help_text='Use the format: In a long and adventurous battle...')),
                ('player1_before_game_elo', models.IntegerField()),
                ('player2_before_game_elo', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('verb', models.CharField(max_length=20, unique=True)),
                ('python_function', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            model_name='match',
            name='outcome',
            field=models.ForeignKey(to='elonomics.Outcome'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='player1',
            field=models.ForeignKey(to='elonomics.Player', related_name='player1'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='player2',
            field=models.ForeignKey(to='elonomics.Player', related_name='player2'),
            preserve_default=True,
        ),
    ]
