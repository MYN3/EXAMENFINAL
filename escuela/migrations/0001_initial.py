# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Imparte',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('grado', models.ForeignKey(to='escuela.Grado')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('profesor', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='imparte',
            name='materia',
            field=models.ForeignKey(to='escuela.Materia'),
        ),
        migrations.AddField(
            model_name='grado',
            name='materias',
            field=models.ManyToManyField(through='escuela.Imparte', to='escuela.Materia'),
        ),
    ]
