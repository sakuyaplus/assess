# Generated by Django 3.2.5 on 2021-07-24 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True)),
                ('user_name', models.IntegerField(blank=True)),
                ('teacher_id', models.IntegerField()),
                ('stars', models.IntegerField()),
                ('message', models.TextField(blank=True)),
                ('comment_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
