from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):

    return render(request, 'board/index.html') # return render()는 html로 넘기겠다는 의미 뒤에 ''는 templates

def list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html',{
        'articles' : articles,
    })

def detail(request, id):
    article = Article.objects.get(id = id)
    return render(request, 'board/detail.html', {
        'article': article,
    })

def new(request):
    return render(request, 'board/new.html')

def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('board:detail', article.id)
    