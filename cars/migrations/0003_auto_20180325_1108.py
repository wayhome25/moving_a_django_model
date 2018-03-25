# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-25 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        # custom migration 을 먼저 수행한 이후에 해당 migration을 실행하도록 dependency를 변경한다
        ('cars', '0002_auto_20180325_1112'),
        # Make certain the tires db state is setup
        ('tires', '0001_initial.py'),
    ]

    # 해당 마이그레이션은 모델 FK 를 변경했을때 자동으로 생성된 것이다.
    # We need to remove the DeleteModel operation because that model exists in state only.
    operations = [
        migrations.AlterField(
            model_name='car',
            name='tires',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.Tires'),
        ),

        # tires 모델 삭제는 다음 마이그레이션에서 수행한다
    ]
