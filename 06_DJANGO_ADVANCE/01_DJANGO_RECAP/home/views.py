from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def guess(request):
    return render(request, 'home/guess.html')
    
def answer(request):
    count = 0
    if request.GET.get('q1') == '1108':
        count += 1
    if request.GET.get('q2') == '부산':
        count += 1
    if request.GET.get('q3') == '리버풀':
        count += 1
    if request.GET.get('q4') == '레드':
        count += 1
    

    #채점
    return render(request, 'home/answer.html', {'count' : count })
