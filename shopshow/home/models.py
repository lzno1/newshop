from django.db import models
import datetime


# Create your models here.
class HotGoods(models.Model):
    goodID = models.CharField('商品ID', max_length=100, blank=True, null=True)
    goodType = models.CharField('主页展示类型', max_length=100, blank=True, null=True)
    goodUrl = models.CharField('商品图片网址', max_length=100, blank=True, null=True)
    goodPrice = models.CharField('商品价格展示', max_length=100, blank=True, null=True)
    goodName = models.CharField('商品名称', max_length=100, blank=True, null=True)
    

class BannerShow(models.Model):
    bannerImg = models.CharField('主页展示图片地址', max_length=100, blank=True, null=True)
    bannerUrl = models.CharField('点击跳转到的网址', max_length=100, blank=True, null=True)




