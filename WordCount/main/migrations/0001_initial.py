# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 05:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site', models.URLField(primary_key=True, serialize=False)),
                ('checked_date', models.DateTimeField(verbose_name='date checked')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('word', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('word_type', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='WordSoup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Site')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Word')),
            ],
        ),
    ]