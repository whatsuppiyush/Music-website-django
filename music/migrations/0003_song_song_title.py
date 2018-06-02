# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180601_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_title',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
