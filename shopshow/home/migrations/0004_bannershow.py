# Generated by Django 3.1.3 on 2023-04-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230412_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerImg', models.CharField(blank=True, max_length=100, null=True, verbose_name='主页展示图片地址')),
                ('bannerUrl', models.CharField(blank=True, max_length=100, null=True, verbose_name='点击跳转到的网址')),
            ],
        ),
    ]
