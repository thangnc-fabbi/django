from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from . import models


class TodoListView(View):
    model = models.TodoModel

    def get_queryset(self):
        return models.TodoModel.objects.filter(is_deleted=False).all()

    def get(self, request):
        todo = self.get_queryset()
        return render(request, 'todo/index.html', {'todos': todo})


class CreateTodoView(View):
    model = models.TodoModel

    def post(self, request, **kwargs):
        data = request.POST
        if data['todo_text'] == '' or data['todo_text'] == None:
            pass
        else:
            models.TodoModel.objects.create(content=data['todo_text'])
        return redirect(reverse('todo_template'))


class UpdateTodoView(View):
    model = models.TodoModel

    def post(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            todo = models.TodoModel.objects.get(id=pk)
            todo.completed = True if not todo.completed else False
            todo.save()
        return redirect(reverse('todo_template'))


class DeleteTodoView(View):
    model = models.TodoModel

    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            todo = models.TodoModel.objects.get(id=pk)
            todo.delete()
        return redirect(reverse('todo_template'))
