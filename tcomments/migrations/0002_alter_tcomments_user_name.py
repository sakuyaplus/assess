# Generated by Django 3.2.5 on 2021-07-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcomments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tcomments',
            name='user_name',
            field=models.CharField(max_length=100),
        ),
    ]
