# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-28 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_add_url_fields_in_profile_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_avatar',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
