from django.shortcuts import render
from .models import Stores
from .models import logistics
# Create your views here.
def store(request):
    stores = Stores.objects.all()
    return render(request, 'store.html', {'stores': stores})

def uplog(request):
    if request.POST:
        if 'goodSave' in request.POST:
            try:
                goodid = request.POST['goodid']
                tranid = request.POST['tranid']
                check1 = request.POST['check1']
                check2 = request.POST['check2']
                check3 = request.POST['check3']
                check4 = request.POST['check4']
                check5 = request.POST['check5']
                tran1 = request.POST['tran1']
                tran2 = request.POST['tran2']
                tran3 = request.POST['tran3']
                tran4 = request.POST['tran4']
                tran5 = None
                eva1 = request.POST['eva1']
                eva2 = request.POST['eva2']
                eva3 = request.POST['eva3']
                eva4 = None
                eva5 = None
                logistics.objects.create(goodid=goodid, tranid=tranid, 
                                        check1=check1, check2=check2, check3=check3, check4=check4, check5=check5, 
                                        tran1=tran1, tran2=tran2, tran3=tran3, tran4=tran4, tran5=tran5, 
                                        eva1=eva1, eva2=eva2, eva3=eva3, eva4=eva4, eva5=eva5)
                return render(request, 'UploadLogistics.html', {'logging':'成功保存订单'})
            except:
                return render(request, 'UploadLogistics.html', {'logging':'未能成功保存订单'})
        elif 'googDelete' in request.POST:
            try:
                goodid = request.POST['goodid']
                logistics.objects.filter(goodid=goodid).delete()
                return render(request, 'UploadLogistics.html', {'logging':'成功删除id对应订单'})
            except:
                return render(request, 'UploadLogistics.html', {'logging':'未能删除id对应订单'})
        elif 'googSearch' in request.POST:
            try:
                good_id = request.POST['goodid']
                good_info = logistics.objects.get(goodid = good_id)
                if good_info:
                    return render(request, 'UploadLogistics.html', {'good_info':good_info,'logging':'已查询到对应订单'})
            except:
                return render(request, 'UploadLogistics.html', {'logging':'未查询到id对应订单'})
        
        elif 'googNew' in request.POST:
            try:
                goodid = request.POST['goodid']
                logistics.objects.create(goodid=goodid)
                good_info = logistics.objects.get(goodid = goodid)
                return render(request, 'UploadLogistics.html', {'good_info':good_info,'logging':'新建订单信息'})
            except:
                return render(request, 'UploadLogistics.html', {'logging':'新建订单信息失败'})
    return render(request, 'UploadLogistics.html')