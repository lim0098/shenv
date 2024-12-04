from django.db import models

# Create your models here.

#采购项目
class ProcurementProject(models.Model):
    date=models.CharField(verbose_name='日期',max_length=50)
    title=models.CharField(verbose_name='项目',max_length=50)
    shuliang=models.DecimalField(verbose_name='数量',max_digits=15,decimal_places=4,default=0,blank=True, null=True)
    danjia=models.DecimalField(verbose_name='单价',max_digits=15,decimal_places=4,default=0,blank=True, null=True)
    hanshuijine=models.DecimalField(verbose_name='含税金额',max_digits=15,decimal_places=2)
    shuie=models.DecimalField(verbose_name='税额',max_digits=15,decimal_places=2)

    class Meta:
        verbose_name_plural='采购项目'

    def __str__(self):
        return '%s期间的采购' % (self.date)
    
 #销售项目
class SalesProject(models.Model):
    date=models.CharField(verbose_name='日期',max_length=50)
    title=models.CharField(verbose_name='项目',max_length=50)
    shuliang=models.DecimalField(verbose_name='数量',max_digits=15,decimal_places=4,default=0,blank=True, null=True)
    danjia=models.DecimalField(verbose_name='单价',max_digits=15,decimal_places=4,default=0,blank=True, null=True)
    hanshuijine=models.DecimalField(verbose_name='含税金额',max_digits=15,decimal_places=2)
    shuie=models.DecimalField(verbose_name='税额',max_digits=15,decimal_places=2)

    class Meta:
        verbose_name_plural='销售项目'

    def __str__(self):
        return '%s期间的销售' % (self.date)
    