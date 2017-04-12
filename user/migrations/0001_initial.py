# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-29 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=100)),
                ('name_surname', models.CharField(default='', max_length=100)),
                ('license_id', models.CharField(default='', max_length=100)),
                ('geo_loc', models.CharField(default='', max_length=100)),
                ('username', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('profile_pic', models.ImageField(default='*', upload_to='')),
                ('info', models.CharField(default='*', max_length=150)),
                ('address', models.CharField(default='*', max_length=100)),
                ('tel_num', models.CharField(default='*', max_length=50)),
                ('facebooklink', models.CharField(default='*', max_length=200)),
                ('twitterlink', models.CharField(default='*', max_length=200)),
                ('instagramlink', models.CharField(default='*', max_length=200)),
                ('menu', models.ImageField(default='*', upload_to='')),
                ('reg_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]