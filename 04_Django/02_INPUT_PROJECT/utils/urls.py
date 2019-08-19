from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('art/', views.art),
    path('output/', views.output),
    # path('translate/', views.translate), #utils/translate/
    # path('result/', views.result),  #utils/result/
    path('throw/', views.throw),
    path('catch/', views.catch)
]