from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # /board/ == board:index
    # path('', views.index, name='index'),
    # read 글 목록 render
    path('articles/', views.article_list, name = 'article_list'),
    # read 글 상세 render
    path('articles/<int:article_id>/', views.article_detail, name = 'article_detail'),
    # create 글 쓰기 new render
    path('articles/new/', views.new_article, name='new_article'),
    # Update 글 수정하기(edit)
    path('articles/<int:article_id>/edit/', views.edit_article, name = 'edit_article'),
    # Update 글 실제 수정 update
    # path('articles/<int:id>/update/', views.update, name = 'update'),
    #Del   
    path('aritcles/<int:article_id>/delete/', views.delete_article, name = 'delete_article'),
    #Comment Create
    path('articles/<int:article_id>/comments/new/', views.new_comment, name = 'new_comment'),
    path('articles/<int:article_id>/comments/<int:comment_id>/delete/', views.delete_comment, name ='delete_comment' )
]