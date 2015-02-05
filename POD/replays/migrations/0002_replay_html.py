# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('replays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='replay',
            name='html',
            field=models.CharField(default=4, max_length=400),
            preserve_default=False,
        ),
    ]
