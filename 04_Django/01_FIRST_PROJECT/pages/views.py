from django.shortcuts import render, HttpResponse
import json
# Create your views here.

def index(request):
    return HttpResponse('hi django :)')

def about(request):
    me = {
        'name' : '박민기',
        'role' : 'student',
        'e-mail' : 'minki120@naver.com'
    }
    return HttpResponse(json.dumps(me))

#HTML 을 내보내고 싶다.
def portfolio(request):

    return render(request, 'portfolio.html')

def help(request):
    
    return render(request, 'help.html')