from django.db import models


class Customer(models.Model):
    company_name = models.CharField(max_length=50, default='', verbose_name='公司名称')
    fax_number = models.CharField(max_length=20, verbose_name='传真号码')
    company_number = models.CharField(max_length=20, verbose_name='公司号码')
    batch_number = models.CharField(max_length=100, verbose_name='批号')

    class Meta:
        verbose_name_plural = verbose_name = '客户信息'

    def __str__(self):
        return self.company_name
