# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='web',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.TextField()),
                ('link', models.URLField()),
                ('visitno', models.BigIntegerField()),
                ('time', models.DateTimeField()),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
    ]
