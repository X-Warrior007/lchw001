# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_auto_20180128_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('parent', models.ForeignKey(blank=True, null=True, to='Book.AreaInfo')),
            ],
            options={
                'db_table': 'areainfo',
            },
        ),
    ]
