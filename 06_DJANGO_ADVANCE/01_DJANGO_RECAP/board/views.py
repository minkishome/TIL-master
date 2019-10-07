from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from .models import Article
# Create your views here.

@require_GET
def index(request):

    return render(request, 'board/index.html') # return render()는 html로 넘기겠다는 의미 뒤에 ''는 templates

@require_GET
def list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html',{
        'articles' : articles,
    })


@require_GET
def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'board/detail.html', {
        'article': article,
    })

@require_GET
def new(request):
    return render(request, 'board/new.html')

@require_POST
def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('board:detail', article.id)


@require_GET
def edit(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'board/edit.html', {
        'article': article,
    })
    
@require_POST
def update(request, id):
    article = get_object_or_404(Article, id=id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('board:detail', article.id)

@require_POST
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('board:list')