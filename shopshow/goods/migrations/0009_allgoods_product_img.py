# Generated by Django 3.1.3 on 2023-03-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20230311_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='allgoods',
            name='Product_img',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
