# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-31 16:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_places'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Places',
            new_name='Place',
        ),
        migrations.DeleteModel(
            name='CustomerTest',
        ),
        migrations.RemoveField(
            model_name='message',
            name='username',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]