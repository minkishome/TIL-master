from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'board/index.html') # return render()는 html로 넘기겠다는 의미 뒤에 ''는 templates
