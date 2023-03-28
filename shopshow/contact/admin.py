from django.contrib import admin
from .models import FAQuestion
from .models import MessageBoard
from .models import ProductRequest
# Register your models here.

class QuestionInfo(admin.ModelAdmin):
    list_display = ['title', 'answer']

class MessageBoardInfo(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'company', 'phone', 'email', 'contact', 'create_time']

class ProductRequestInfo(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'company', 'phone', 'product_name', 'product_code', 'date', 'quantity', 'contact', 'create_time']

admin.site.register(FAQuestion, QuestionInfo)
admin.site.register(MessageBoard, MessageBoardInfo)
admin.site.register(ProductRequest, ProductRequestInfo)