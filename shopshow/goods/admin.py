from django.contrib import admin
from .models import ALLHotGoods
from .models import Dingdans
from .models import selectDingdans
from .models import CaiGou
from .models import AllGoods
# Register your models here.
class HotGoodsInfo(admin.ModelAdmin):
    list_display = ['name', 'price', 'url', 'img']

class DingdansINFO(admin.ModelAdmin):
    list_display = ['index', 'pi', 'kehu', 'goods', 'user', 'money', 'poID', 'poTime', 'label']


class SelectDingdansINFO(admin.ModelAdmin):
    list_display = ['time', 'username', 'dingdanname', 'upmoney', 'pi', 'com', 'dingdanID', 'type', 'num', 'money', 'othermoney', 'allmoney']

class CaiGouInfo(admin.ModelAdmin):
    list_display = ['time', 'user', 'goods', 'upMoney', 'PI', 'com', 'phone', 'type', 'num', 'money', 'otherMoney', 'allMoney']

class AllGoodsInfo(admin.ModelAdmin):
    list_display = ['create_time','Product_Name', 'Product_Number', 'Product_img', 'Product_IsHazmat', 'Description', 'Summary', 'Product_Type', 'Category', 'Keywords', 'Product_Color', 'Material', 'Size_Group', 'Size_Values', 'Shape', 'Theme', 
                    'Origin', 'Imprint_Method', 'Imprint_Color', 'Imprint_Size', 'Imprint_Location', 'Price_Includes', 'Sequence', 'Currency', 'Always_Free_Setup', 'Upcharge_Name', 'Upcharge_Criteria_1', 'Upcharge_Criteria_2', 'Upcharge_Type', 'Upcharge_Level', 'Service_Charge', 'Upcharge_Details',  
                    'UQ1', 'UQ2', 'UQ3', 'UQ4', 'UQ5', 'UQ6', 'UQ7', 'UQ8', 'UQ9', 'UQ10', 
                    'UP1', 'UP2', 'UP3', 'UP4', 'UP5', 'UP6', 'UP7', 'UP8', 'UP9', 'UP10', 
                    'UD1', 'UD2', 'UD3', 'UD4', 'UD5', 'UD6', 'UD7', 'UD8', 'UD9', 'UD10', 
                    'Production_Time', 'Rush_Service', 'Rush_Time', 'Same_Day_Service', 'Packaging', 'Shipping_Items', 'Shipping_Dimensions', 'Shipping_Weight', 'Shipper_Bills_By', 'Shipping_Info', 'Free_Shipping', 
                    'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 
                    'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 
                    'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 
                    'Distributor_View_Only', 'Carrier_Information', 'Market_Segment']

admin.site.register(ALLHotGoods, HotGoodsInfo)
admin.site.register(Dingdans, DingdansINFO)
admin.site.register(selectDingdans, SelectDingdansINFO)
admin.site.register(CaiGou, CaiGouInfo)
admin.site.register(AllGoods, AllGoodsInfo)