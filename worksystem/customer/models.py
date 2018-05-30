from django.db import models


class Customer(models.Model):
    company_name = models.CharField(verbose_name='公司名称', max_length=50, default='')
    fax_number = models.CharField(verbose_name='传真号码', max_length=20)
    company_number = models.CharField(verbose_name='公司号码', max_length=20)
    batch_number = models.CharField(verbose_name='批号', max_length=100)

    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.company_name
