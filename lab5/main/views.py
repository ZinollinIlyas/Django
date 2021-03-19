from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import *
from django.db.models import Prefetch

from .serializers import *


class TodoListView(generics.ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer


class TaskListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TasksGetSerializer

    def get_queryset(self):
        return Todos.objects.all().prefetch_related(Prefetch('tasks', queryset=Tasks.objects.filter(mark=False)))


class CompletedListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Tasks.objects.filter(mark=True)
    serializer_class = TasksSerializer
