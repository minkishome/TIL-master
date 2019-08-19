from django.urls import path
from . import views

urlpatterns = [
    #Domain/board/index/
    #Create
    path('articles/new/' , views.new), #/board/articles/new/
    path('articles/create/', views.create), #/board/articles/create
    path('articles/modify/', views.modify),
    # Read
    path('articles/', views.index), #/board/articles/
    path('articles/<int:article_id>/', views.show),  #/board/articles/
    #Update
    #Delete
    path('articles/<int:article_id>/delete/', views.delete) #board/article/article.id/delete


]
