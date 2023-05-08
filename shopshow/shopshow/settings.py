"""
Django settings for shopshow project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7-8wsqi(eq3wri62b$33bmzq_)^6jmwf7m&_-src+b$0y_nons'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# ALLOWED_HOSTS = ['108.61.220.238']
# ALLOWED_HOSTS = ['127.0.0.1']
# ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'contact',
    'goods',
    'store',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shopshow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shopshow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# DEBUG = False
# ALLOWED_HOSTS = ['www.promo-union.com','promo-union.com','108.61.220.238']
# # ALLOWED_HOSTS = ['127.0.0.1']
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# debug
DEBUG = True
ALLOWED_HOSTS = ['*']
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SIMPLEUI_HOME_INFO = False

SIMPLEUI_CONFIG = {
    'system_keep':False,
    'menu_display':['订单管理', '采购与物流管理', '客户管理', '留言与任务', '页面自定义', '权限管理'],
    'dynamic':False,
    'menus':[
        {
            'app':'goods',
            'name': '订单管理',
            'models': [
            {
                'name': '订单查询',
                'url': '/admin/goods/selectdingdans/'
            },
            {
                'name': '订单基本信息',
                'url': '/admin/goods/dingdans/'
            },
            {
                'name': '商品信息',
                'url': '/admin/goods/allgoods/'
            }
        ]
        },
        {
            'app': 'goods',
            'name': '采购与物流管理',
            'models':[
                {
                'name': '采购信息',
                'url': '/admin/goods/caigou/'
                },
                {
                'name': '物流信息',
                'url': '/admin/store/logistics/'
                },
            ]
        },

        {
            'app': 'store',
            'name': '客户管理',
            'models':[
                {
                'name': '客户黑名单',
                'url': '/admin/store/customblacklist/'
                },
                {
                'name': '客户等级查询',
                'url': '/admin/store/customlevel/'
                },
                {
                'name': '客户明细表',
                'url': '/admin/store/custominfo/'
                },
            ]
        },

        {
            # 'app': 'admin',
            'name': '留言与任务',
            'models':[
                {
                    'name': '留言板',
                    'url': '/admin/contact/messageboard/'
                },
                {
                    'name': '商品问询',
                    'url': '/admin/contact/productrequest/'
                },
                {
                    'name': '邮箱提交',
                    'url': '/admin/home/emailsubmit/'
                },
                {
                'name': '任务列表',
                'url': 'tasks/task/'
                },
            ]
        },

        {
            # 'app': 'admin',
            'name': '页面自定义',
            'models':[
                {
                    'name': '介绍问答',
                    'url': '/admin/contact/faquestion/'
                },
                {
                    'name': '主页商品展示',
                    'url': '/admin/home/hotgoods/'
                },
                {
                    'name': '主页banner展示',
                    'url': '/admin/home/bannershow/'
                },
            ]
        },

        {
            'app':'auth',
            'name': '权限管理',
            'models': [
            {
                'name': '用户列表',
                'url': 'auth/user/'
            },
            {
                'name': '用户分组',
                'url': 'auth/group/'
            }
        ]
        },
    ]

}