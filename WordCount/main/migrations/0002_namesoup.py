# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 05:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameSoup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Name')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Site')),
            ],
        ),
    ]
