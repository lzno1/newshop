# Generated by Django 3.1.3 on 2023-04-12 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_auto_20230412_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='allgoods',
            name='create_time',
            field=models.DateField(default=datetime.date.today, verbose_name='提交日期'),
        ),
    ]
