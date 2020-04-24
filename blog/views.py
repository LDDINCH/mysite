test1 001
test2 002
from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogType
from read_record.models import ReadNum, ReadDetail
from pure_pagination import Paginator,  PageNotAnInteger
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    blog_dates = Blog.objects.dates('createtime', 'year', order='DESC')
    blog_dates_counts = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(createtime__year=blog_date.year).count()
        blog_dates_counts[blog_date] = blog_count

    context['blog_dates'] = blog_dates_counts
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(context['blogs'], 3, request=request)

    context['page_of_blogs'] = p.page(page)
    return render(request,'blog_list.html', context)

def blog_detail(request, blog_id):
    context = {}
    blog = get_object_or_404(Blog, id=blog_id)
    context['blog'] = blog

    if not request.COOKIES.get('blog_%s_readed' % blog_id):
        ct = ContentType.objects.get_for_model(Blog)
        if ReadNum.objects.filter(content_type=ct, object_id=blog.id).count():
           readnum = ReadNum.objects.get(content_type=ct, object_id=blog.id)
        else:
            readnum = ReadNum(content_type=ct, object_id=blog.id)
        readnum.read_num +=1
        readnum.save()
        date = timezone.now().date()
        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=blog.id, date=date)
        readDetail.read_num +=1
        readDetail.save()
    context['blog'].save()
    context['previous_blog'] = Blog.objects.filter(createtime__gt=context['blog'].createtime).last()
    context['next_blog'] = Blog.objects.filter(createtime__lt=context['blog'].createtime).first()
    response = render(request,'blog_detail.html', context)
    response.set_cookie('blog_%s_readed' % blog_id, 'true')
    return response

def blog_type_list(request, blog_type_id):
    context = {}
    blog_type = get_object_or_404(BlogType, id=blog_type_id)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    blog_dates = Blog.objects.dates('createtime', 'year', order='DESC')
    blog_dates_counts = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(createtime__year=blog_date.year).count()
        blog_dates_counts[blog_date] = blog_count

    context['blog_dates'] = blog_dates_counts
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(context['blogs'], 3, request=request)

    context['page_of_blogs'] = p.page(page)
    return render(request,'blog_type_list.html', context)

def blog_with_dates(request, year, month):
    context = {}
    context['blogs'] = Blog.objects.filter(createtime__year=year)
    context['blog_types'] = BlogType.objects.all()
    blog_dates = Blog.objects.dates('createtime', 'year', order='DESC')
    blog_dates_counts = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(createtime__year=blog_date.year).count()
        blog_dates_counts[blog_date] = blog_count

    context['blog_dates'] = blog_dates_counts
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(context['blogs'], 3, request=request)

    context['page_of_blogs'] = p.page(page)
    return render(request,'blog_with_dates.html', context)


# Create your views here.
