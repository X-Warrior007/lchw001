# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_auto_20180128_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'peopleinfo',
            },
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='commentcount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='readcount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='book',
            field=models.ForeignKey(to='Book.BookInfo'),
        ),
    ]
