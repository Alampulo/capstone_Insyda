# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoods', '0005_profile_neighbourhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='display',
            field=models.ImageField(default='groups/group.png', upload_to='groups/'),
        ),
    ]
