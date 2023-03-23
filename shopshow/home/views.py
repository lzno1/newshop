from cgitb import html
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from .models import HotGoods
from store.models import logistics
from goods.models import AllGoods

# Create your views here.
def home(request):
    if request.method == "POST":
        if 'goodid' in request.POST:
            goodid = request.POST['goodid']
            try:
                info = AllGoods.objects.get(Product_Number=goodid)
                return render(request, 'goodInfo.html',{'info':info})
            except:
                hotgoods = HotGoods.objects.all()
                return render(request, 'home.html',{'hotgoods': hotgoods, 'ERROR':'商品ID错误'})
        elif 'logisticsid' in request.POST:
            goodid = request.POST['logisticsid']
            try:
                logInfo = logistics.objects.get(goodid=goodid)
                hotgoods = HotGoods.objects.all()
                return render(request, 'home.html',{'hotgoods': hotgoods,'logInfo':logInfo})
            except:
                hotgoods = HotGoods.objects.all()
                return render(request, 'home.html',{'hotgoods': hotgoods,'logError':'订单ID错误'})
    else:
        hotgoods = HotGoods.objects.all()
        return render(request, 'home.html',{'hotgoods': hotgoods})



 
