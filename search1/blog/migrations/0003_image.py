# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_web'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word1', models.TextField()),
                ('link', models.URLField()),
                ('link2', models.ImageField(upload_to=b'')),
                ('visitno1', models.BigIntegerField()),
                ('time1', models.DateTimeField()),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
    ]
