# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_auto_20150122_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='bodyEvent',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
