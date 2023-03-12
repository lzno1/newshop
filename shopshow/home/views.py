from cgitb import html
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import HotGoods
from store.models import logistics

# Create your views here.
def home(request):
    if request.method == "POST":
        goodid = request.POST['id']
        logInfo = logistics.objects.get(goodid=goodid)
        hotgoods = HotGoods.objects.all()
        return render(request, 'home.html',{'hotgoods': hotgoods,'logInfo':logInfo})
    else:
        hotgoods = HotGoods.objects.all()
        return render(request, 'home.html',{'hotgoods': hotgoods})



 
