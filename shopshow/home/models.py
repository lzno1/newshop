from django.db import models

# Create your models here.
class HotGoods(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='img/', blank=True)

