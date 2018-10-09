# _*_ encoding:utf-8 _*_
__author__ = "ludada"
__date__ = "2018/9/27 23:11"
import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum, ReadDetail

def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums

def get_today_read_data(content_type):
    today = timezone.now().date()
    read_detail = ReadDetail.objects.filter(content_type=content_type, date=today).order_by('-read_num')
    return read_detail
def get_yestoday_read_data(content_type):
    yestoday = timezone.now().date() - datetime.timedelta(days=1)
    read_detail = ReadDetail.objects.filter(content_type=content_type, date=yestoday).order_by('-read_num')
    return read_detail