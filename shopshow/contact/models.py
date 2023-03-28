from django.db import models
import datetime

# Create your models here.
class FAQuestion(models.Model):
    title = models.CharField('问题', max_length=128, blank=True, null=True)
    answer = models.CharField('回答', max_length=512, blank=True, null=True)

class MessageBoard(models.Model):
    fname = models.CharField(max_length=40, blank=True, null=True)
    lname = models.CharField(max_length=40, blank=True, null=True)
    company = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    contact = models.CharField(max_length=400, blank=True, null=True)
    create_time = models.DateField('提交日期',default=datetime.date.today)

class ProductRequest(models.Model):
    fname = models.CharField('first name', max_length=40, blank=True, null=True)
    lname = models.CharField('last name', max_length=40, blank=True, null=True)
    email = models.CharField('email', max_length=40, blank=True, null=True)
    company = models.CharField('company', max_length=64, blank=True, null=True)
    phone = models.CharField('phone', max_length=20, blank=True, null=True)
    product_name = models.CharField('商品名称' ,max_length=64, blank=True, null=True)
    product_code = models.CharField('商品代码', max_length=10, blank=True, null=True)
    date = models.DateField('计划日期',default=datetime.date.today)
    quantity = models.CharField('需求数量', max_length=40, blank=True, null=True)
    contact = models.CharField('留言内容',max_length=400, blank=True, null=True)
    create_time = models.DateField('提交日期',default=datetime.date.today)
