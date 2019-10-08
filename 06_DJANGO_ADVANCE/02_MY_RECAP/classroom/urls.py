from django.urls import path
from . import views


app_name = 'classroom'

urlpatterns = [
    path('', views.index, name='index'),
    # read 글 목록 render
    path('students/', views.list, name = 'list'),
    # read 글 상세 render
    path('students/<int:id>/', views.detail, name = 'detail'),
    # create 글 쓰기 new render
    path('students/new/', views.new, name='new'),
    # create 글 저장 create
    path('students/create/', views.create, name='create'),
    # Update 글 수정하기(edit)
    path('students/<int:id>/edit/', views.edit, name = 'edit'),
    # Update 글 실제 수정 update
    path('students/<int:id>/update/', views.update, name = 'update'),
    #Del   
    path('students/<int:id>/delete/', views.delete, name = 'delete'),

]