# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-04 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_avatar',
            field=models.ImageField(upload_to='./media'),
        ),
    ]
