from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # /board/ == board:index
    path('', views.index, name='index'),
    # read 글 목록 render
    path('articles/', views.list, name = 'list'),
    # read 글 상세 render
    path('articles/<int:id>/', views.detail, name = 'detail'),
    # create 글 쓰기 new render
    path('articles/new/', views.new, name='new'),
    # Update 글 수정하기(edit)
    path('articles/<int:id>/edit/', views.edit, name = 'edit'),
    # Update 글 실제 수정 update
    #path('articles/<int:id>/update/', views.update, name = 'update'),
    #Del   
    path('aritcles/<int:id>/delete/', views.delete, name = 'delete'),

]