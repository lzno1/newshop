from cgitb import html
from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse,HttpResponseRedirect,redirect
from .models import HotGoods
from .models import BannerShow
from .models import EmailSubmit
from .models import PONumber
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
# 判断设备信息
import re


def judge_pc_or_mobile(ua):
    """
    判断访问来源是pc端还是手机端
    :param ua: 访问来源头信息中的User-Agent字段内容
    :return:
    """

    factor = ua
    is_mobile = False

    _long_matches = r'googlebot-mobile|android|avantgo|blackberry|blazer|elaine|hiptop|ip(hone|od)|kindle|midp|mmp' \
                    r'|mobile|o2|opera mini|palm( os)?|pda|plucker|pocket|psp|smartphone|symbian|treo|up\.(browser|link)' \
                    r'|vodafone|wap|windows ce; (iemobile|ppc)|xiino|maemo|fennec'
    _long_matches = re.compile(_long_matches, re.IGNORECASE)
    _short_matches = r'1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)' \
                     r'|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)' \
                     r'|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw' \
                     r'|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8' \
                     r'|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit' \
                     r'|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)' \
                     r'|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji' \
                     r'|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|e\-|e\/|\-[a-w])|libw|lynx' \
                     r'|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi' \
                     r'|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)' \
                     r'|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg' \
                     r'|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21' \
                     r'|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-' \
                     r'|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it' \
                     r'|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)' \
                     r'|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)' \
                     r'|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit' \
                     r'|wi(g |nc|nw)|wmlb|wonu|x700|xda(\-|2|g)|yas\-|your|zeto|zte\-'

    _short_matches = re.compile(_short_matches, re.IGNORECASE)

    if _long_matches.search(factor) != None:
        is_mobile = True
    user_agent = factor[0:4]
    if _short_matches.search(user_agent) != None:
        is_mobile = True

    return is_mobile



# Create your views here.
def home(request):
    re_title = request.META.get("HTTP_USER_AGENT")
    is_mobile = judge_pc_or_mobile(re_title)
    if is_mobile:
        print('手机访问')
    allBanners = BannerShow.objects.all()
    if request.method == "POST":
        hotgoods = HotGoods.objects.all()
        if 'goodid' in request.POST:
            allgoods = AllGoods.objects.all()
            goodid = request.POST['goodid']
            long_num = 0
            letter_num = 0
            number_num = 0
            for s in goodid:
                if s.isalpha():
                    letter_num += 1
                    long_num += 1
                elif s.isdigit():
                    number_num += 1
                    long_num += 1

            if (long_num == len(goodid)) and (letter_num > 1) and (number_num > 1):
                try:
                    goodid = goodid.upper()
                    info = AllGoods.objects.get(Product_Number=goodid)
                    return redirect('/goodInfo/?test=a&goodid=' + goodid)
                    # return render(request, 'goodInfo.html',{'info':info})
                except:
                    if is_mobile:
                        return render(request, 'home_m.html',{'hotgoods': hotgoods, 'banner':allBanners, 'ERROR':'Item not found'})
                    return render(request, 'home.html',{'hotgoods': hotgoods, 'banner':allBanners, 'ERROR':'Item not found'})
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
                    if is_mobile:
                        return render(request, 'home_m.html',{'hotgoods': hotgoods, 'banner':allBanners, 'ERROR':'Item not found'})
                    return render(request, 'home.html',{'hotgoods': hotgoods, 'banner':allBanners,  'ERROR':'Item not found'})
                else:
                    return redirect('/goods/' + goodid)
                    # page = Paginator(newgoods, 25)
                    # page_obj = page.get_page(0)
                    # # redirect('/goods/All/')
                    # return render(request, 'goods.html', {'goods': page_obj, 'goodid':goodid})
        
        elif 'logisticsid' in request.POST:
            goodid = request.POST['logisticsid']
            if not goodid.startswith('#'):
                goodid = '#' + goodid
            try:
                PONumberInfo = PONumber.objects.get(poNumber=goodid)
                hotgoods = HotGoods.objects.all()
                if is_mobile:
                    return render(request, 'home_m.html',{'hotgoods': hotgoods, 'banner':allBanners, 'poInfo':PONumberInfo})
                return render(request, 'home.html',{'hotgoods': hotgoods, 'banner':allBanners, 'poInfo':PONumberInfo})
            except:
                hotgoods = HotGoods.objects.all()
                if is_mobile:
                    return render(request, 'home_m.html',{'hotgoods': hotgoods, 'banner':allBanners, 'logError':'Item not found'})
                return render(request, 'home.html',{'hotgoods': hotgoods, 'banner':allBanners, 'logError':'Item not found'})
            # else:
            #     try:
            #         logInfo = logistics.objects.get(goodid=goodid)
            #         hotgoods = HotGoods.objects.all()
            #         # return render(request, 'home.html',{'hotgoods': hotgoods, 'banner':allBanners, 'logInfo':logInfo})
            #         return render(request, 'home.html',{'hotgoods': hotgoods, 'banner':allBanners})
            #     except:
            #         hotgoods = HotGoods.objects.all()
            #         return render(request, 'home.html',{'hotgoods': hotgoods, 'banner':allBanners, 'logError':'Item not found'})
        
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
            # sendEmail('主页留言板', email_content, '1176530132@qq.com')
            hotgoods = HotGoods.objects.all().values()
            allgoods = AllGoods.objects.all()
            hotGoodInfo = {'Swag_Stuff':[], 'Seasonal_Items':[], 'New_Peomo':[], 'Holidays_Related':[]}
            for good in hotgoods.iterator():
                if good['goodType'] in hotGoodInfo.keys():
                    # print(good)
                    hotGoodInfo[good['goodType']].append(good)
            if is_mobile:
                return render(request, 'home_m.html',{'hotgoods': hotGoodInfo, 'banner':allBanners})
            return render(request, 'home.html',{'hotgoods': hotGoodInfo, 'banner':allBanners})
        elif 'submit_email' in request.POST:
            # print('submit_email')
            allBanners = BannerShow.objects.all()
            hotgoods = HotGoods.objects.all().values()
            hotGoodInfo = {'Swag_Stuff':[], 'Seasonal_Items':[], 'New_Peomo':[], 'Holidays_Related':[]}
            for good in hotgoods.iterator():
                if good['goodType'] in hotGoodInfo.keys():
                    # print(good)
                    hotGoodInfo[good['goodType']].append(good)
            email_name = request.POST['email_request']
            try:
                EmailSubmit.objects.filter(email=email_name)
            except:
                pass
            EmailSubmit.objects.create(email=email_name)
            if is_mobile:
                return render(request, 'home_m.html',{'hotgoods': hotGoodInfo, 'banner':allBanners})
            return render(request, 'home.html',{'hotgoods': hotGoodInfo, 'banner':allBanners})


    else:
        hotgoods = HotGoods.objects.all().values()
        allgoods = AllGoods.objects.all()
        hotGoodInfo = {'Swag_Stuff':[], 'Seasonal_Items':[], 'New_Peomo':[], 'Holidays_Related':[]}
        for good in hotgoods.iterator():
            if good['goodType'] in hotGoodInfo.keys():
                # print(good)
                hotGoodInfo[good['goodType']].append(good)
        if is_mobile:
            return render(request, 'home_m.html',{'hotgoods': hotGoodInfo, 'banner':allBanners})
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
    # print('邮件发送成功')
    smtpObject.quit()
 
