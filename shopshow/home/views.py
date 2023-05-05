from cgitb import html
from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse,HttpResponseRedirect,redirect
from .models import HotGoods
from .models import BannerShow
from store.models import logistics
from goods.models import AllGoods
from contact.models import MessageBoard
from django.http import HttpResponse,Http404,FileResponse
from django.conf import settings
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# Create your views here.
def home(request):
    allBanners = BannerShow.objects.all()
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
                    return render(request, 'home.html',{'hotgoods': hotgoods, 'banner':allBanners, 'ERROR':'商品ID错误'})
            else:
                allgoods = AllGoods.objects.all()
                goods = allgoods.values("Product_Name","Product_Number","P1","Product_img","Category","Keywords","Description")
                newgoods = []
                for good in goods.iterator():
                    if good['Category']:
                        # if category in good['Category']:
                        if (goodid.lower() in good['Product_Name'].lower()) or (goodid.lower() in good['Keywords'].lower()):
                            newgoods.append(good)
                if len(newgoods) == 0:
                    return render(request, 'home.html',{'hotgoods': hotgoods, 'banner':allBanners,  'ERROR':'未找到商品'})
                else:
                    page = Paginator(newgoods, 25)
                    page_obj = page.get_page(0)
                    # redirect('/goods/All/')
                    return render(request, 'goods.html', {'goods': page_obj, 'goodid':goodid})
        
        elif 'logisticsid' in request.POST:
            goodid = request.POST['logisticsid']
            try:
                logInfo = logistics.objects.get(goodid=goodid)
                hotgoods = HotGoods.objects.all()
                return render(request, 'home.html',{'hotgoods': hotgoods, 'banner':allBanners, 'logInfo':logInfo})
            except:
                hotgoods = HotGoods.objects.all()
                return render(request, 'home.html',{'hotgoods': hotgoods, 'banner':allBanners, 'logError':'订单ID错误'})
        
        elif 'submit_to_me' in request.POST:
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            company = request.POST['company']
            phone = request.POST['phone']
            email = request.POST['email']
            contact = request.POST['contact']
            MessageBoard.objects.create(fname=fname,lname=lname,company=company,phone=phone,email=email,contact=contact)
            email_content = 'firstname: ' + fname + '<br/>lastname: ' + lname + '<br/>company: ' + company + '<br/>phone: ' + phone + '<br/>email: ' + email + '<br/>comments: ' + contact
            sendEmail('主页留言板', email_content, 'support@promo-union.com')
            hotgoods = HotGoods.objects.all().values()
            allgoods = AllGoods.objects.all()
            hotGoodInfo = {'Swag_Stuff':[], 'Seasonal_Items':[], 'New_Peomo':[], 'Holidays_Related':[]}
            for good in hotgoods.iterator():
                if good['goodType'] in hotGoodInfo.keys():
                    print(good)
                    hotGoodInfo[good['goodType']].append(good)
            return render(request, 'home.html',{'hotgoods': hotGoodInfo, 'banner':allBanners})
    else:
        hotgoods = HotGoods.objects.all().values()
        allgoods = AllGoods.objects.all()
        hotGoodInfo = {'Swag_Stuff':[], 'Seasonal_Items':[], 'New_Peomo':[], 'Holidays_Related':[]}
        for good in hotgoods.iterator():
            if good['goodType'] in hotGoodInfo.keys():
                print(good)
                hotGoodInfo[good['goodType']].append(good)
        return render(request, 'home.html',{'hotgoods': hotGoodInfo, 'banner':allBanners})


def downsq(request):
    # print(str(settings.BASE_DIR))
    file_path = os.path.join(settings.BASE_DIR, 'db.sqlite3') 
    try:
        f = open(file_path,"rb")
        r = FileResponse(f,as_attachment=True,filename="sqlite.sqlite3")
        return r
    except Exception:
        raise Http404("Download error")
    
    return render(request, 'UploadGoods.html')

def sendEmail(title, email_content, mail_receivers):
    mail_host = "smtp.163.com"
    mail_sender = 'm18831899513@163.com'
    mail_license = 'UTKLVKJXVESYHXTX'
    # mail_receivers = 'wj18831899513@gmail.com'

    # 带有附件时
    # mm = MIMEMultipart('')

    msg = MIMEMultipart()
    msg['From'] = mail_sender
    msg['To'] = mail_receivers
    msg['Subject'] = Header(title, 'utf-8')

    message = MIMEText(email_content, 'html', 'utf-8')

    msg.attach(message)

    smtpObject = smtplib.SMTP()
    smtpObject.connect(mail_host, 25)
    # 打印SMTP服务器交互信息
    # smtpObject.set_debuglevel(1)
    smtpObject.login(mail_sender, mail_license)
    smtpObject.sendmail(mail_sender, mail_receivers, msg.as_string())
    print('邮件发送成功')
    smtpObject.quit()
 
