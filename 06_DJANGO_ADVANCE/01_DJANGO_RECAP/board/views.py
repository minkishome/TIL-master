from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article, Comment

from .forms import ArticleModelForm

from IPython import embed
# CRUD
# 사실 get, post 두 개 뿐 아니라 비공식 http method 방식이 겁나 많아
# 그래서 다른 method 를 통해 들어 올 수 없도록 제한을 두는 것
@require_http_methods(['GET', 'POST'])
def new_article(request):
    # 요청이 GET / POST 인지 확인한다.
    # 만약 POST 라면
    if request.method == 'POST':
        # ArticleModelForm 의 instance 생성하고, Data를 채운다(Binding 'bound=True').
        form = ArticleModelForm(request.POST)
        # Binding 된 form 이 유효한지 체크한다.
        if form.is_valid():
            # 유효하다면 form 을 저장한다.
            article = form.save()
            # 저장한 article 로 redirect 한다.
            return redirect(article) # == redirect('board:article_detail', article.id)  
         # else 문은 밑에 중복되니까 생략 가능
        # 유효하지 않는 form 이라면
        # else:
        #     # 유효하지 않은 입력 데이터를 담은 html 과 에러메시지를 사용자에게 보여준다.
        #     return render(request, 'board/new.html', {
        #         'form': form,
        #     })

    # 만약 GET 이라면
    else:
        # 비어있는 form(html 생성기) 을 만든다.
        form = ArticleModelForm()
        # form 과 html 을 사용자에게 보여준다.
    return render(request, 'board/new.html', {
        'form': form,
    })

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html',{
        'articles' : articles,
    })


@require_http_methods(['GET', 'POST'])
def edit_article(request, article_id):
    article = get_object_or_404(Article, id = article_id)

    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article) # 제출받은 요청
        if form.is_valid:
            article = form.save()
            return redirect(article)
        else:
            form = ArticleModelForm(instance = article)
        return render(request, 'board/edit.html',{
            'form' : form,
        })


        # return redirect(aritcle)

def article_detail(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    comments = article.comment_set.all().reverse()
    return render(request, 'board/detail.html',{
        'article' : article,
        'comments' : comments,
    })
    # return redirect(aritcle)


@require_POST
def delete_article(request, article_id):
    article = get_object_or_404(Article, id= article_id)
    aritcle.delete()
    return redirect('board:article_list')

@require_POST
def new_comment(request, article_id):  
    article = get_object_or_404(Article, id = article_id)
    comment = Comment()
    comment.content = request.POST.get('comment_content')
    comment.article_id = article.id
    comment.save()
    return redirect(article)