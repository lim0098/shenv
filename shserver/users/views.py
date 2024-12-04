import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import re
from rest_framework_simplejwt.exceptions import TokenError,InvalidToken,status 
from django.http import  HttpResponse,JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication 
from rest_framework_simplejwt.views import TokenViewBase 
from django.core.serializers import serialize
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

##
from .serializers import MyTokenSerializer,RoleSerializer,MenuSerializer
from users.models import User ,Role,Menu

# Create your views here.


# 角色视图
class RoleViewsSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    # authentication_classes = [authentication.JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,DjangoFilterBackend,)
    # search_fields =['date']
    # filterset_fields = ['date']


# 菜单视图
class MenuViewsSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # authentication_classes = [authentication.JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,DjangoFilterBackend,)
    # search_fields =['date']
    # filterset_fields = ['date']


# 用户注册接口
class RegisterViews(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        email=request.data.get('email')
        password_confirmation=request.data.get('password_confirmation')
        if not all([username,password,email,password_confirmation]):
            return Response({'error':'参数不能为空'},status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error':'用户名已存在'},status=status.HTTP_400_BAD_REQUEST)
        if password!=password_confirmation:
            return Response({'error':'两次密码不一致'},status=status.HTTP_400_BAD_REQUEST)
        if not(6<=len(password)<=18):
            return Response({'error':'密码长度应在6至18直接'},status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'error':'该邮箱已被其他用户使用'},status=status.HTTP_400_BAD_REQUEST)
        # if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}{1,2}$)',email):
        if not re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',email):
            return Response({'error':'邮箱格式有误'},status=status.HTTP_400_BAD_REQUEST)
        obj=User.objects.create_user(username=username,email=email,password=password)
        res={'username':obj.username,'id':obj.id,'email':obj.email}
        return Response(res,status=status.HTTP_201_CREATED)
    
 
##  不需要携带token就能访问接口
def ListShops(requests):
    return HttpResponse("this is shop list")
 
# 测试
class DetailsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication)
 
    def get(self, request, *args, **kwargs):
        print('authenticate: ', request.successful_authenticator.authenticate(request))
        print('token信息: ', request.successful_authenticator.get_validated_token(
            request.successful_authenticator.get_raw_token(request.successful_authenticator.get_header(request))))
        print('登录用户: ', request.successful_authenticator.get_user(request.successful_authenticator.get_validated_token(
            request.successful_authenticator.get_raw_token(request.successful_authenticator.get_header(request)))))
        return Response('get ok')
 
    def post(self, request, *args, **kwargs):
        return Response('post ok')
 
from django.contrib.auth.models import Permission


# 自定义的登陆视图
class LoginView(TokenViewBase):
    serializer_class = MyTokenSerializer  # 使用刚刚编写的序列化类
 
    # post方法对应post请求，登陆时post请求在这里处理
    def post(self, request, *args, **kwargs):
        # 使用刚刚编写时序列化处理登陆验证及数据响应
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise ValueError(f'验证失败： {e}')
        result=serializer.validated_data
        # 获取指定用户
        user = User.objects.get(pk=serializer.user.id)
        # 获取该用户的所有权限
        permissions = user.user_permissions.select_related('content_type')
        # 获取用户通过组获得的权限
        group_permissions = Permission.objects.filter(group__user=user)
        
        # 合并用户直接赋予和通过组赋予的权限
        all_permissions = list(set(list(permissions) + list(group_permissions)))
        
        # print(all_permissions)
        # 创建一个包含内容类型名称的字典
        content_type_names = {ct.id: ct.name for ct in ContentType.objects.all()}
        # 序列化权限并添加内容类型名称
        p=[]
        # serialized_permissions = serialize('json', permissions, fields=('content_type', 'codename'))
        serialized_permissions = serialize('json', all_permissions)
        for permission in json.loads(serialized_permissions):
            permission['fields']['content_type_name'] = content_type_names[permission['fields']['content_type']]
            p.append(permission['fields'])
        result['p']=p
        # 获取指定用户
        # user = User.objects.get(pk=serializer.user.id)
        # 获取该用户的所有菜单
        menus = user.menus.all()
        # 获取用户通过组获得的菜单
        role_menus = Menu.objects.filter(role__user=user)       
        # 合并用户直接赋予和通过组赋予的菜单
        all_menus = list(set(list(menus) + list(role_menus)))
        # 序列化权限并添加内容类型名称
        m=[]
        serialized_menus = serialize('json', all_menus)
        for menu in json.loads(serialized_menus):
            m.append(menu['fields']['title'])
        result['m']=m
        print(m)
        return Response(result, status=status.HTTP_200_OK)
 
 