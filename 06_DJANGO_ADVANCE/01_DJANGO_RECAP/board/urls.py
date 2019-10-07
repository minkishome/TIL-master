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
    # create 글 저장 create
    path('articles/create/', views.create, name='create'),
    

]