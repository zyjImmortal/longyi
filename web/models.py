from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Advisory(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50)
    body = RichTextField(verbose_name='内容')
    author = models.CharField(verbose_name='作者', max_length=50)

    class Meta:
        verbose_name = '资讯'
        verbose_name_plural = '资讯'


class Product(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50)
    author = models.CharField(verbose_name='作者', max_length=50)
    produce = models.CharField(verbose_name='产区', max_length=50)
    capacity = models.CharField('干型 含量', help_text='单位：ml', max_length=50)
    degree = models.CharField('度数', help_text='单位：%vol', max_length=50)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'
