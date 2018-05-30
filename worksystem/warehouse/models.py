# coding:utf-8

from django.db import models

from customer.models import Customer


class Warehouse(models.Model):
    '''
    仓库
    '''
    STATUS_CHOICES = (
        ('making', '制作中'),
        ('complete', '已完成'),
        ('outbound', '已出库'),
    )

    batch_number = models.CharField(max_length=50, verbose_name='批号')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='客户')
    version = models.CharField(max_length=100, verbose_name='型号')
    claim = models.TextField(help_text='填写正确的要求', verbose_name='工艺要求')
    length = models.IntegerField(verbose_name='长')
    width = models.IntegerField(verbose_name='宽')
    height = models.IntegerField(verbose_name='高')
    parties = models.IntegerField(verbose_name='方数')
    meters = models.IntegerField(verbose_name='米数')
    product_time = models.DateTimeField(auto_now_add=True, verbose_name='计划生产日期')
    ship_time = models.DateTimeField(auto_now_add=True, verbose_name='出货日期')
    status = models.CharField(choices=STATUS_CHOICES, default='making', max_length=8,  verbose_name='出货明细')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = verbose_name = '仓库信息'

    def __str__(self):
        return self.version












