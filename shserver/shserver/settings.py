"""
Django settings for shserver project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b3l46v8@55%ucumy=a_q%%w$i2dzw6a%ab=)#)-&7=$_#l&eay'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.3']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'users',
    'taxdisplay',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'shserver.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'1234',
        'NAME': 'shserver',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

#允许所有的用户跨域请求
CORS_ORIGIN_ALLOW_ALL=True
# 允许的方法
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
 
# 允许的头
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',  # 添加这一行以允许authentication请求头
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
# 修改语言
LANGUAGE_CODE = 'zh-hans'

# 修改时间
TIME_ZONE = 'Asia/Shanghai'
# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 指定自定义用户类
AUTH_USER_MODEL='users.User'

# 全局配置
REST_FRAMEWORK={
#     # 设置所有接口都需要被验证
  'DEFAULT_PERMISSION_CLASSES': (
      # 设置所有接口都需要被验证
       'rest_framework.permissions.IsAuthenticated',  # 默认权限为验证用户
  ),
    #jwt认证
    'DEFAULT_AUTHENTICATION_CLASSES':(
        # 使用rest_framework_simplejwt验证身份
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS':(
        'django_filters.rest_framework.DjangoFilterBackend',
    )
}

#设置token有效期
SIMPLE_JWT={
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=50),   # 设置token有效时间
    # 'ACCESS_TOKEN_LIFETIME': timedelta(days=7),   # 设置token有效时间
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  # 刷新token有效时间
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    # 'UPDATE_LAST_LOGIN': False,  # 设置为True会在用户登录时，更新user表中的last_login字段

    'ALGORITHM': 'HS256',  # 加密算法
    # 'SIGNING_KEY': settings.SECRET_KEY,  # 签名密钥
    'SIGNING_KEY': SECRET_KEY,  # 签名密钥
    'VERIFYING_KEY': None,  # 验证密钥，用于验证生成令牌的内容
    'AUDIENCE': None,  # 设置为None时，此字段将从token中排除，并且不会进行验证
    'ISSUER': None,  # 设置为None时，此字段将从token中排除，并且不会进行验证
    # 'JWK_URL': None,  # 设置为None时，此字段将从token中排除，并且在验证期间不使用
    # 'LEEWAY': 0,  # 用来给到期时间留一些余地

    'AUTH_HEADER_TYPES': ('Bearer',),  # 认证的标签头，类似jwt token中的jwt
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',  # 身份验证的授权标头名称
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',  # 生成token中声明将用于存储用户标识符
    # 'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_TYPE_CLAIM': 'token_type',  # 用于存储token类型的声明名称

    # 'JTI_CLAIM': 'jti',  # 用于存储令牌的唯一标识符的声明名称

    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}