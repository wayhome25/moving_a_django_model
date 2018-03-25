# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-25 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Make this depend on your FIRST custom cars migration (테이블명 변경)
        ('cars', '0002_auto_20180325_1112.py'),
    ]

    # Convert "operations" to only be "state_operations"
    state_operations = [
        # Theses migrations were auto-generated by Django makemigrations.
        migrations.CreateModel(
            name='Tires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='브랜드명')),
                ('size', models.FloatField(default=17.0, verbose_name='사이즈')),
            ],
        ),
    ]

    operations = [
        # state_operations 만 실행함으로써, 장고가 database에 마이그레이션을 적용했다고 생각하게 할 수 있다.
        # 실제로는 cars_tires 테이블을 tires_tires로 이름을 변경한 것이다.
        migrations.SeperateDatabaseAndState(state_operations=state_operations)
    ]
