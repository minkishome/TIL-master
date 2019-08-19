from django.shortcuts import render, HttpResponse


# Create your views here.
def info(request):
    return render(request, 'info.html')

   

def student(request, name):
    student_info = {
        '홍길동' : 20 ,
        '박길동' : 19,
        '김길동' : 28
    }
    context = {'name' : name, 'age' : student_info[name]}
    return render(request, 'cube.html', context)