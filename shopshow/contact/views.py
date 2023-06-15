from django.shortcuts import render
from .models import FAQuestion
from .models import MessageBoard
from django.shortcuts import HttpResponse,HttpResponseRedirect,redirect
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# Create your views here.
def contact(request):
    questions = FAQuestion.objects.all()
    if request.method == "POST":
        # 商品询问信息留言
        if 'commit_request' in request.POST:
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            company = request.POST['company']
            phone = request.POST['phone']
            email = request.POST['email']
            contact = request.POST['contact']
            MessageBoard.objects.create(fname=fname,lname=lname,company=company,phone=phone,email=email,contact=contact)
            email_content = 'firstname: ' + fname + '<br/>lastname: ' + lname + '<br/>company: ' + company + '<br/>phone: ' + phone + '<br/>email: ' + email + '<br/>comments: ' + contact
            sendEmail('主页留言板', email_content, 'support@promo-union.com')
            
            return redirect('/')
    return render(request, 'contact.html', {'faqs':questions})

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