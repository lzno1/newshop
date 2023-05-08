from django.contrib import admin
from .models import HotGoods
from .models import BannerShow
from .models import EmailSubmit
from store.models import logistics
# Register your models here.


class HotGoodsInfo(admin.ModelAdmin):
    list_display = ['goodID', 'goodType', 'goodUrl', 'goodName', 'goodPrice']

class BannerShowInfo(admin.ModelAdmin):
    list_display = ['bannerImg', 'bannerUrl']

class EmailInfo(admin.ModelAdmin):
    list_display = ['email']
# class LogisticsInfo(admin.ModelAdmin):
#     list_display = ['goodid', 'tranid', 
#                     'check1', 'check2', 'check3', 'check4', 'check5', 
#                     'tran1', 'tran2', 'tran3', 'tran4', 'tran5', 
#                     'eva1', 'eva2', 'eva3', 'eva4', 'eva5']

admin.site.site_title = '用户名'
admin.site.register(HotGoods, HotGoodsInfo)
admin.site.register(BannerShow, BannerShowInfo)
admin.site.register(EmailSubmit, EmailInfo)
# admin.site.register(logistics, LogisticsInfo)