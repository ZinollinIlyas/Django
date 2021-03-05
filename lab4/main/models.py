from django.db import models


class Todos(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    task = models.CharField(max_length=50, null=True)
    created_at = models.DateField(null=True)
    due_on = models.DateField(null=True)
    owner = models.CharField(max_length=50)
    mark = models.BooleanField(null=True)
    todos = models.ForeignKey(Todos, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
