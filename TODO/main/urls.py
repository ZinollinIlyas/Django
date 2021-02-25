from django.urls import path
from .views import index, todos, completed_tasks

urlpatterns = [
    path('', index),
    path('todos/', todos),
    path('todos/completed', completed_tasks)

]
