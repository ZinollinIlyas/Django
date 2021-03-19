from rest_framework import serializers

from .models import Todos, Tasks


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class TasksGetSerializer(serializers.ModelSerializer):
    tasks = TasksSerializer(many=True, read_only=True)

    class Meta:
        model = Todos
        fields = ('id', 'name','tasks')
