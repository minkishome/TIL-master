from django.shortcuts import render
from .models import Student
# Create your views here.

def create(request):
    student = Student()
    student.name = request.GET.get('input_name')
    student.eamil = request.GET.get('input_email')
    student.birthday = request.GET.get('input_birthday')
    student.age = request.GET.get('input_age')
    student.save()
    return render(requset, 'board/index.html')