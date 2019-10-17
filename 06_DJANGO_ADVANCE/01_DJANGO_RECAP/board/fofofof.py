from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article, Comment

from .forms import ArticleModelForm, CommentModelForm

@require_http_methods(['GET', 'POST'])
def new_article(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleModelForm()
    return render(request, 'board/new_article.html',{
        'form':form,
    })

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html',{
        'articles' : articles, 
    })

def article_detail(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    comment = article.comment_set.all()
    return render(request, 'board/detail.html',{
        'article':article,
        'comment':comment,
    })

def edit_article(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    if request.method =='POST':
        form = ArticleModelForm(request, instance= article )
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleModelForm(request, instance=article)
    return render(request, 'board/edit.html',{
        'article':article,
    })


def delete_article(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    article.delete()
    return redirect('board:article_list')


def new_comment(request, article_id):
    article = get_object_or_404(Article, id= article_id)
    form = CommentModelForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article_id = article_id
        comment.save()
        
        return redirect(article)

def delete_comment(request, article_id, comment_id):
    comment = get_object_or_404(Comment, comment_id)
    comment.delete()
    return redirect(article)

