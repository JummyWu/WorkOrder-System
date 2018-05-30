# coding:utf-8

from django.db import models

from customer import Customer


class Warehouse(models.Model):
    '''
    仓库
    '''
    batch_number = models.CharField(max_length=50, verbose_name='批号')
    customer = models.ForeignKey(Customer, verbose_name='客户')
    version = models.CharField(max_length=100, verbose_name='型号')
    claim = models.TextField(help_text='填写正确的要求', verbose_name='工艺要求')
    length = models.IntegerField(max_length=10, verbose_name='长')
    width = models.IntegerField(max_length=10, verbose_name='宽')
    height = models.IntegerField(max_length=10, verbose_name='高')
    parties = models.IntegerField(max_length=10, verbose_name='方数')
    meters = models.IntegerField(max_length=10, verbose_name='米数')
    add_tiem = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.version

    class Meta:
        verbose_name = verbose_name_plural = '仓库信息'
