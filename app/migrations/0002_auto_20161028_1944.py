# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 19:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='transactions',
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='action',
            field=models.CharField(choices=[('W', 'Withdrawal'), ('D', 'Deposit')], max_length=2),
        ),
    ]