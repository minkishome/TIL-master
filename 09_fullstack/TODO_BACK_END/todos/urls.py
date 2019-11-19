from django.urls import path
from . import views


app_name = "todos" # 필요없음

urlpatterns = [
    path('', views.create_todo ),
    # PATCH api/v1/todos/1 => update1 || DELETE 
    path('<int:todo_id>/', views.update_delete_todo),
    ]
