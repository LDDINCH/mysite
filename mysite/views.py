from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from read_record.utils import get_seven_days_read_data, get_today_read_data, get_yestoday_read_data
from blog.models import Blog
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegForm
from django.contrib.auth.models import User
from utils.email_send import send_register_email
from comment.models import EmailVerifyRecord

def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_read_datas'] = get_today_read_data(blog_content_type)
    context['yestoday_read_datas'] = get_yestoday_read_data(blog_content_type)
    return render(request,'home.html', context)

def userlogin(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            if user.is_active:
                auth.login(request, user)
                return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)

def active(request, active_code):
    all_records = EmailVerifyRecord.objects.filter(code=active_code)
    if all_records:
        for record in all_records:
            email = record.email
            user = User.objects.get(email=email)
            user.is_active = True
            user.save()
    else:
        return render(request, 'active_fail.html')
    return redirect(reverse('login'))

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.is_active = False
            user.save()
            send_register_email(email, 'register')
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)
