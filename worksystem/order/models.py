from django.db import models
from customer.models import Customer


class Order(models.Model):
    # 订货日期
    order_time = models.DateTimeField(auto_now_add=True, verbose_name='订货日期')
    # 型号
    version = models.CharField(verbose_name='型号', max_length=100)
    # 物品长
    length = models.IntegerField(verbose_name='长', max_length=10, default=10)
    # 物品宽
    width = models.IntegerField(verbose_name='宽', max_length=10, default=10)
    # 物品高
    height = models.IntegerField(verbose_name='高', max_length=10, default=10)
    # 订单件数
    number = models.IntegerField(verbose_name='件数', max_length=10, default=1)
    # 工艺要求
    requirement = models.CharField(verbose_name='工艺要求', max_length=200)
    # 下单人地址
    address = models.CharField(verbose_name='订单地址', max_length=200)
    # 计划生产
    plan_product = models.CharField(verbose_name='计划生产', max_length=200)
    # 客户
    customer = models.ForeignKey(Customer, verbose_name='客户', on_delete=models.CASCADE)
    # 存放位置
    #location = models

    class Meta:
        ordering = ['-order_time']
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    def get_size(self, length, width):
        return length * width

    def __str__(self):
        return self.version


