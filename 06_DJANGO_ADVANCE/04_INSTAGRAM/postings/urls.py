from django.urls import path
from . import views

app_name = 'postings'

#insta
urlpatterns = [
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),
    path('', views.posting_list, name='posting_list'),
    path('create/', views.create_posting, name='create_posting'),
    path('<int:posting_id>/update', views.update_posting, name='update_posting'),
    path('<int:posting_id>/delete', views.delete_posting, name='delete_posting'),

]
