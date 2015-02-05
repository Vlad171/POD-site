# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('replaytitle', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(unique=True, verbose_name=b'slug')),
                ('publishreplay', models.DateTimeField(default=datetime.datetime.now)),
                ('createdreplay', models.DateTimeField(auto_now=True)),
                ('modifiedreplay', models.DateTimeField(auto_now_add=True)),
                ('authorreplay', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'replay',
            },
            bases=(models.Model,),
        ),
    ]
