from django.shortcuts import render
from .models import Todos, Tasks


def index(request):
    return render(request, 'index.html')


def todo_list(request, pk):
    tasks = Tasks.objects.filter(todos=pk, mark=False)
    todos = Todos.objects.get(id=pk)
    context = {
        'tasks': tasks,
        'todos': todos
    }
    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request, id):
    tasks = Tasks.objects.filter(todos=id, mark=True)
    todos = Todos.objects.get(id=id)
    context = {
        'tasks': tasks,
        'todos': todos
    }

    return render(request, 'completed_todo_list.html', context=context)


def todos(request):
    todos = Todos.objects.all()
    context = {
        'todos': todos
    }

    return render(request, 'todos.html', context=context)
