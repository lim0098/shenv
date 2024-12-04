# users.models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# 菜单表
class Menu(models.Model):
    titlecode=models.CharField(verbose_name='菜单编码',help_text='例如:01-01',max_length=50)
    title=models.CharField(verbose_name='菜单名',max_length=50)
    url=models.CharField(verbose_name='含正则URL路径',max_length=64)
    
    class Meta:
        verbose_name_plural='菜单表'
    def __str__(self):
        return self.title

# 角色表
class Role(models.Model):
    title=models.CharField(verbose_name='角色名',max_length=50)
    menus = models.ManyToManyField(
        Menu,
        verbose_name="菜单",
        blank=True,
    )
    
    class Meta:
        verbose_name_plural='角色表'
    def __str__(self):
        return self.title
    
    
# 用户表
class User(AbstractUser):
    create_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time=models.DateTimeField(verbose_name='更新时间',auto_now=True)
    is_delete=models.BooleanField(verbose_name='删除标记',default=False)
    mobile=models.CharField(verbose_name='手机号',help_text='手机号',max_length=11,default='',blank=True)
    avatar=models.ImageField(verbose_name='头像url',help_text='头像',max_length=30,default='',blank=True)
    menus = models.ManyToManyField(
        Menu,
        verbose_name="菜单",
        blank=True,
    )
    roles = models.ManyToManyField(
        Role,
        verbose_name="角色",
        blank=True,
    )
    class Meta:
        verbose_name_plural='用户表'
        db_table='users'

     