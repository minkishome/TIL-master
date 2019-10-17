from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #(인증용 form)
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
# Create your views here.
 
@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated: #user가 login한 상태라면 무시
        return redirect('sns:posting_list')      
    #사용자가 회원가입할 데이터를 보냈다면,
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('sns:posting_list')
        # else:
        #     return render(request, 'accounts/signup.html', {
        #         'form':form, 
        #     })
    else: # 사용자가 회원가입 HTML을 달라는 뜻
        form = UserCreationForm()

    return render(request, 'accounts/signup.html',{
        'form':form, 
    })

@require_http_methods(['GET','POST'])
def login(request):
    # from IPython import embed; embed()
  


    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) #다른것과 다르게 Authentic은 첫번째 인자가 request다. 
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('sns:posting_list')
            
             
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form':form, 
    })    


def logout(request):
    auth_logout(request)
    return redirect('sns:posting_list')