from django.db import models
from customer.models import Customer


class Order(models.Model):
    order_time = models.DateTimeField(auto_now_add=True, verbose_name='订货日期')
    version = models.CharField(max_length=100, verbose_name='型号')
    length = models.IntegerField(max_length=10, default=10, verbose_name='长')
    width = models.IntegerField(max_length=10, default=10, verbose_name='宽')
    height = models.IntegerField(max_length=10, default=10, verbose_name='高')
    parties = models.IntegerField(max_length=10, verbose_name='方数')
    meters = models.IntegerField(max_length=10, verbose_name='米数')
    number = models.IntegerField(max_length=10, default=1, verbose_name='件数')
    requirement = models.CharField(max_length=200, verbose_name='工艺要求')
    address = models.CharField(max_length=200, verbose_name='订单地址')
    plan_product = models.CharField(max_length=200, verbose_name='计划生产')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='客户')

    class Meta:
        ordering = ['-order_time']
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    def get_size(self, length, width):
        return length * width

    def __str__(self):
        return self.version
