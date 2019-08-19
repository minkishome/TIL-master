from django.urls import path
from . import views


#utils/
urlpatterns = [
      #D/utils/cube/<정수>/  <>안은 고정값이 아님을 의미 /는 무조건 뒤에
    path('cube/<int:num>/', views.cube) ,
    #check_int/<정수>/
    path('check_int/<int:num>/', views.check_int),

    # #pick_lotto/
    path('pick_lotto/', views.pick_lotto)
]
