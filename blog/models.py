# _*_ encoding:utf-8 _*_

from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from read_record.models import ReadNum
from django.db.models.fields import exceptions

class BlogType(models.Model):
    type_name = models.CharField(max_length = 15)

    class Meta:
        verbose_name=u'博客类型'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=30)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    createtime = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-createtime']
        verbose_name=u'博客'
        verbose_name_plural = verbose_name
    def get_read_num(self):
        ct = ContentType.objects.get_for_model(Blog)
        try:
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.id)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0


    def __str__(self):
        return "<Blog: %s>" % self.title

# class ReadNum(models.Model):
#     read_num = models.IntegerField(default=0, verbose_name=u'博客阅读数')
#     blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
#

