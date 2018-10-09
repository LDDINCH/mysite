from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
import datetime
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0, verbose_name=u'博客阅读数')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = u'阅读数'
        verbose_name_plural = verbose_name

class ReadDetail(models.Model):
    date = models.DateTimeField(default=timezone.now)
    read_num = models.IntegerField(default=0, verbose_name=u'博客阅读数')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = u'时间段阅读数'
        verbose_name_plural = verbose_name



# Create your models here.
