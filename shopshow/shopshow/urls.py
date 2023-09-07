"""shopshow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.views import static
from django.conf.urls import url
from django.urls import re_path
from django.urls import path
from contact.views import contact
from goods.views import goods
from goods.views import allgoods
from goods.views import showAllGoodPage
from goods.views import showAllGood
from home.views import home, UpdateBannerTool, UpdateShowgoodsTool, UpdateAllGoodsTool
from home.views import getJsonByHomeData, getJsonByGoodsData
from home.views import downsq
# from store.views import store
from goods.views import goodInfo
from store.views import uplog


urlpatterns = [
    path('aecihrydbfsakm/', admin.site.urls),
    path('home/', home, name='home'),
    path('', home, name='home'),
    path('goods/', showAllGoodPage, name='goods'),
    path('goods/<category>/', showAllGood),
    # re_path('^goods/$', showAllGood, name='newgoods'),
    re_path('^goodInfo/$', goodInfo, name='goodInfo'),
    path('contact/', contact, name='contact'),
    path('uplogpromo/', uplog, name='uploadLogistics'),
    path('upgoodpromo/', allgoods, name='uploadGoods'),
    path('addToolGetJsonByHome/', getJsonByHomeData, name='getJsonByHomeData'),
    path('addToolGetJsonByGoods/', getJsonByGoodsData, name='getJsonByGoodsData'),
    path('addToolUpdateBanner/<info>/', UpdateBannerTool, name='UpdateBannerTool'),
    path('addToolUpdateShowgoods/<info>/', UpdateShowgoodsTool, name='getJsonByGoodsData'),
    path('addToolUpdateAllGoods/<info>/', UpdateAllGoodsTool, name='getJsonByGoodsData'),
    path('downloadDataMysqlbd/', downsq, name='downsq'),
    url(r'^static/(?P<path>.*)$', static.serve,
      {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(?P<path>.*)$',static.serve,{'document_root':settings.MEDIA_ROOT}),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
# if settings.DEBUG is False:
#     urlpatterns += patterns( ' ',url(r'^static/(?P.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,}),)