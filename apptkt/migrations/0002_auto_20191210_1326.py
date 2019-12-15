# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-10 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apptkt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('siren', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca', models.IntegerField()),
                ('margin', models.IntegerField()),
                ('ebitda', models.IntegerField()),
                ('loss', models.IntegerField()),
                ('year', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptkt.Company')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
