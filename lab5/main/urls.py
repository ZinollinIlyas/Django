from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view()),
    path('<int:pk>/', views.TaskListView.as_view()),
    path('<int:pk>/completed/', views.CompletedListView.as_view())
]