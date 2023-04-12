from cgitb import html
from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse,HttpResponseRedirect
from .models import HotGoods
from store.models import logistics
from goods.models import AllGoods
from contact.models import MessageBoard

# Create your views here.
def home(request):
    if request.method == "POST":
        hotgoods = HotGoods.objects.all()
        if 'goodid' in request.POST:
            allgoods = AllGoods.objects.all()
            goodid = request.POST['goodid']
            long_num = 0
            for s in goodid:
                if (s.isupper()) or (s.isdigit()):
                    long_num += 1
            if long_num == len(goodid):
                try:
                    info = AllGoods.objects.get(Product_Number=goodid)
                    return render(request, 'goodInfo.html',{'info':info})
                except:
                    return render(request, 'home.html',{'hotgoods': hotgoods, 'ERROR':'商品ID错误'})
            else:
                allgoods = AllGoods.objects.all()
                goods = allgoods.values("Product_Name","Product_Number","P1","Product_img","Category","Keywords","Description")
                newgoods = []
                for good in goods.iterator():
                    if good['Category']:
                        # if category in good['Category']:
                        if (goodid in good['Product_Name']) or (goodid in good['Description']) or (goodid in good['Keywords']):
                            newgoods.append(good)
                if len(newgoods) == 0:
                    return render(request, 'home.html',{'hotgoods': hotgoods, 'ERROR':'未找到商品'})
                else:
                    page = Paginator(newgoods, 25)
                    page_obj = page.get_page(0)
                    return render(request, 'goods.html', {'goods': page_obj, 'goodid':goodid})
        
        elif 'logisticsid' in request.POST:
            goodid = request.POST['logisticsid']
            try:
                logInfo = logistics.objects.get(goodid=goodid)
                hotgoods = HotGoods.objects.all()
                return render(request, 'home.html',{'hotgoods': hotgoods,'logInfo':logInfo})
            except:
                hotgoods = HotGoods.objects.all()
                return render(request, 'home.html',{'hotgoods': hotgoods,'logError':'订单ID错误'})
        
        elif 'submit_to_me' in request.POST:
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            company = request.POST['company']
            phone = request.POST['phone']
            email = request.POST['email']
            contact = request.POST['contact']
            logistics.objects.create(fname=fname,lname=lname,company=company,phone=phone,email=email,contact=contact)
            
    else:
        hotgoods = HotGoods.objects.all().values()
        allgoods = AllGoods.objects.all()
        hotGoodInfo = {'Swag_Stuff':[], 'Seasonal_Items':[], 'New_Peomo':[], 'Holidays_Related':[]}
        for good in hotgoods.iterator():
            if good['goodType'] in hotGoodInfo.keys():
                print(good)
                hotGoodInfo[good['goodType']].append(good)
        return render(request, 'home.html',{'hotgoods': hotGoodInfo})



 
