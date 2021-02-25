from datetime import datetime

from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def todos(request):
    tasks = [
        {
            'name': 'Task1',
            'created': datetime(2018, 9, 10).strftime('%d/%m/%Y'),
            'due': datetime(2018, 9, 12).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'done'
        },
        {
            'name': 'Task 2',
            'created': datetime(2018, 9, 10).strftime("%d/%m/%Y"),
            'due': datetime(2018, 9, 12).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'done'
        },
        {
            'name': 'Task 3',
            'created': datetime(2018, 9, 10).strftime("%d/%m/%Y"),
            'due': datetime(2018, 9, 12).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'done'
        },
        {
            'name': 'Task 4',
            'created': datetime(2018, 9, 10).strftime("%d/%m/%Y"),
            'due': datetime(2018, 9, 12).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'done'
        }
    ]

    context = {
        'tasks': tasks
    }

    return render(request, 'todo_list.html', context=context)

def completed_tasks(request):
    tasks = [
        {
            'name': 'Task 0',
            'created': datetime(2018, 9, 10).strftime("%d/%m/%Y"),
            'due': datetime(2018, 9, 12).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'Not done'
        }
    ]

    context = {
        'tasks': tasks
    }

    return render(request, 'completed_todo_list.html', context=context)

