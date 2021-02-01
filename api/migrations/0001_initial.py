# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-11-03 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='课程名称')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='模块名称')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course', verbose_name='课程')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='标签')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='视频名称')),
                ('vid', models.CharField(max_length=64, verbose_name='保利威视频ID')),
                ('tag', models.ManyToManyField(to='api.Tag', verbose_name='标签')),
            ],
        ),
    ]
