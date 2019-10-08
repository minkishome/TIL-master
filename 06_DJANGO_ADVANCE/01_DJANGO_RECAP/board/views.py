from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from IPython import embed
from .models import Article
from .forms import ArticleModelForm

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

def new(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        embed()
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleModelForm()
        # return redirect(article)
        # article = Article()
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        # return redirect(article)

    return render(request, 'board/new.html', {
        'form' : form,
    })
        





def edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article = get_object_or_404(Article, id=id)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(article)
        
    else:
       return render(request, 'board/edit.html', {
            'article': article,
        })



@require_POST
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('board:list')