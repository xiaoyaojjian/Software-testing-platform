# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-19 16:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sign', '0007_auto_20160808_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, verbose_name='姓名')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户详情',
                'verbose_name_plural': '用户详情',
            },
        ),
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(max_length=200, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='event',
            name='limit',
            field=models.IntegerField(verbose_name='容纳用户数'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100, verbose_name='发布会名称'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(verbose_name='发布会时间'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.BooleanField(verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.CharField(max_length=16, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='realname',
            field=models.CharField(max_length=64, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='sign',
            field=models.BooleanField(verbose_name='签到状态'),
        ),
    ]
