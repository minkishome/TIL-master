from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm

# Create your views here.
 
@login_required # 로그인이 안되어 있을 경우 무조건 /accounts/login/으로 가라 (login_url='/accounts/login/')
@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html',{
        'postings' : postings,
    })
@login_required
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id = posting_id)
    comments = posting.comments.all()
    is_like = True if posting.likes_users.filter(id=request.user.id).exists() else False
    return render(request, 'sns/posting_detail.html',{  
        'posting': posting,  
        'comments':comments,
        'is_like' : is_like
    })


@login_required
@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES)  # 검증 & 저장 준비
    if form.is_valid():  # 검증!
        posting = form.save(commit=False)  # 저장 => Posting 객체 return
        posting.user = request.user
        posting.save()
        return redirect(posting)  # 성공하면 detail page
    else:
        return redirect('sns:posting_list')  # 실패하면 list page


@login_required
@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES) #검증 & 저장 준비
    if form.is_valid(): #검증
        posting = form.save(commit=False) #저장 => Posting 객체 return
        posting.user = request.user
        posting.save()
        return redirect(posting)
    else:
        return redirect('sns:posting_list')


@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id = posting_id)
    if request.user == posting.user:
        posting.delete()
    return redirect('sns:posting_list')


@login_required
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST) # content만 값을 확인
    if form.is_valid(): # content만 값을 검증
        comment = form.save(commit=False) #아직 posting_id가 비어있기 때문에 저장하는 척만 Comment 객체 return
        comment.posting = posting #comment.posting_id = posting.id
        comment.user = request.user
        comment.save()
    return redirect(posting)


@login_required
@require_POST
def delete_comment(request,posting_id, comment_id):
    comment = get_object_or_404(Comment, posting_id = posting_id,  id = comment_id )
    comment.delete()
    return redirect(comment.posting)


@login_required
@require_POST
def toggle_like(request, posting_id):
    user = request.user
    posting = get_object_or_404(Posting, id = posting_id)
    if posting.likes_users.filter(id=user.id).exists():
        posting.likes_users.remove(user)
    else:
        posting.likes_users.add(user)


    # if user in posting.likes_users.all():
    #     posting.likes_users.remove(user)
    # else:
    #     posting.likes_users.add(user)
    return redirect(posting)

# @login_required
# @require_POST
# def dislike(request, posting_id):
#     user = request.user
#     posting = get_object_or_404(Posting, id = posting_id)
#     posting.likes_users.remove(user)
#     return redirect(posting)
