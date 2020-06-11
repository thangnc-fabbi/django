from django.conf import settings
from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url(r'^', include('todo.api.urls')),
    url(r'todo', views.TodoListView.as_view(), name='todo_template'),
    url(r'create', views.CreateTodoView.as_view(), name='todo_create'),
    url(r'^update/(?P<pk>[0-9]+)/', views.UpdateTodoView.as_view(), name='todo_update'),
    url(r'^delete/(?P<pk>[0-9]+)/', views.DeleteTodoView.as_view(), name='todo_delete'),
]
