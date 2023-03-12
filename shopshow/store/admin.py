from django.contrib import admin
from .models import Stores
from .models import customLevel
from .models import customBlacklist
from .models import customInfo
from .models import logistics
# Register your models here.


class StoresInfo(admin.ModelAdmin):
    list_display = ['name', 'info', 'url', 'img']

class customBlacklistInfo(admin.ModelAdmin):
    list_display = ['index', 'custom', 'email', 'list', 'reason', 'time', 'user', 'remark']

class customLevelInfo(admin.ModelAdmin):
    list_display = ['email', 'level']

class customInfoInfo(admin.ModelAdmin):
    list_display = ['custom', 'email', 'allMoney']

class LogisticsInfo(admin.ModelAdmin):
    list_display = ['goodid', 'tranid', 
                    'check1', 'check2', 'check3', 'check4', 'check5', 
                    'tran1', 'tran2', 'tran3', 'tran4', 'tran5', 
                    'eva1', 'eva2', 'eva3', 'eva4', 'eva5']

admin.site.register(Stores, StoresInfo)
admin.site.register(customBlacklist, customBlacklistInfo)
admin.site.register(customLevel, customLevelInfo)
admin.site.register(customInfo, customInfoInfo)
admin.site.register(logistics, LogisticsInfo)