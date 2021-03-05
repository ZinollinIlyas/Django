from django.urls import path
from .views import index, todo_list, completed_todo_list, todos

urlpatterns = [
    path('', index),
    path('todos/',todos),
    path('todos/<int:pk>', todo_list),
    path('todos/<int:id>/completed', completed_todo_list)
]