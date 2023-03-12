from django.db import models

# Create your models here.
class Stores(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    info = models.TextField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='img/', blank=True)


class customBlacklist(models.Model):
    index = models.CharField(max_length=100, blank=True, null=True)
    custom = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    list = models.CharField(max_length=40, blank=True, null=True)
    reason = models.CharField(max_length=40, blank=True, null=True)
    time = models.CharField(max_length=40, blank=True, null=True)
    user = models.CharField(max_length=40, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)

class customLevel(models.Model):
    email = models.CharField(max_length=40, blank=True, null=True)
    level = models.CharField(max_length=40, blank=True, null=True)
    

class customInfo(models.Model):
    custom = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    allMoney = models.CharField(max_length=40, blank=True, null=True)

class logistics(models.Model):
    goodid = models.CharField(max_length=40, primary_key=True)
    tranid = models.CharField(max_length=40, blank=True, null=True)
    check1 = models.CharField(max_length=40, blank=True, null=True)
    check2 = models.CharField(max_length=40, blank=True, null=True)
    check3 = models.CharField(max_length=40, blank=True, null=True)
    check4 = models.CharField(max_length=40, blank=True, null=True)
    check5 = models.CharField(max_length=40, blank=True, null=True)
    tran1 = models.CharField(max_length=40, blank=True, null=True)
    tran2 = models.CharField(max_length=40, blank=True, null=True)
    tran3 = models.CharField(max_length=40, blank=True, null=True)
    tran4 = models.CharField(max_length=40, blank=True, null=True)
    tran5 = models.CharField(max_length=40, blank=True, null=True)
    eva1 = models.CharField(max_length=40, blank=True, null=True)
    eva2 = models.CharField(max_length=40, blank=True, null=True)
    eva3 = models.CharField(max_length=40, blank=True, null=True)
    eva4 = models.CharField(max_length=40, blank=True, null=True)
    eva5 = models.CharField(max_length=40, blank=True, null=True)


