# 创建model
```python
# users.models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    create_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time=models.DateTimeField(verbose_name='更新时间',auto_now=True)
    is_delete=models.BooleanField(verbose_name='删除标记',default=False)
    mobile=models.CharField(verbose_name='手机号',help_text='手机号',max_length=11,default='',blank=True)
    avatar=models.ImageField(verbose_name='头像url',help_text='头像',max_length=30,default='',blank=True)

    class Meta:
        verbose_name_plural='用户表'
        db_table='users'
```

# 数据库迁移命令
python manage.py makemigrations
python manage.py migrate
# 创建管理员
python manage.py createsuperuser
# 运行
python manage.py runserver