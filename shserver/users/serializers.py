#users.serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
import time

from users.models import User,Role,Menu


from rest_framework import permissions


# 自定义权限，数据作者才有权限
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# 用户序列化器
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        # fields='__all__'
        fields=['id','username','email','mobile','avatar']

# 角色序列化器
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'

# 菜单序列化器
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields='__all__'

 
# 如果自定义了用户表，那么就要使用这个方法来获取用户模型
# 没有自定义的话可以使用以下方式加载用户模型:
# from django.contrib.auth.models import User
 
# 不过这种是万能的
# User = get_user_model()
 
 
# 重写TokenObtainPairSerializer类的部分方法以实现自定义数据响应结构和payload内容
class MyTokenSerializer(TokenObtainPairSerializer):
 
    @classmethod
    def get_token(cls, user):
        """
        此方法往token的有效负载 payload 里面添加数据
        例如自定义了用户表结构，可以在这里面添加用户邮箱，头像图片地址，性别，年龄等可以公开的信息
        这部分放在token里面是可以被解析的，所以不要放比较私密的信息
        :param user: 用戶信息
        :return: token
        """
        token = super().get_token(user)
        # 添加个人信息
        token['name'] = user.username
        return token
 
    def validate(self, attrs):
        """
        此方法为响应数据结构处理
        原有的响应数据结构无法满足需求，在这里重写结构如下：
        {
            "refresh": "xxxx.xxxxx.xxxxx",
            "access": "xxxx.xxxx.xxxx",
            "expire": Token有效期截止时间,
            "username": "用户名",
        }
        :param attrs: 請求參數
        :return: 响应数据
        """
        # data是个字典
        # 其结构为：{'refresh': '用于刷新token的令牌', 'access': '用于身份验证的Token值'}
        data = super().validate(attrs)
 
        # 获取Token对象
        refresh = self.get_token(self.user)
        #加个token的键，值和access键一样
        data['token']=data['access']
        #然后把access键干掉
        del data['access']
        # 令牌到期时间
        timestamp = refresh.access_token.payload['exp']  # 有效期-时间戳
        time_local = time.localtime(int(timestamp))
        data['expire'] = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
 
        # 用户名
        data['username'] = self.user.username
 
        return data