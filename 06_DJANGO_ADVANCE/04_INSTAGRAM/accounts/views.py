from django.shortcuts import render, redirect, get_list_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth import login as auth_login, logout as auth_log_out
# 사용자 회원가입용 Form 과 인증(로그인)용 Form
from .forms import CustomAuthenticationForm, CustomUserCreationForm
# User 라고 import 하면 언제 어떻게 바뀔지 모르니까 변수를 사용하는 게 좋아
# from .models import User​
# 현재 Project 에서 사용할 User 모델을 return 하는 함수
from django.contrib.auth import get_user_model

User = get_user_model()

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form, 
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) 
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })
    
def logout(request):
    auth_log_out(request)
    return redirect('/')