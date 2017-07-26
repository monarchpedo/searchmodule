# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.TextField()),
                ('link', models.URLField()),
                ('link3', models.FileField(upload_to=b'')),
                ('visitno', models.BigIntegerField()),
                ('time', models.DateTimeField()),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
    ]
