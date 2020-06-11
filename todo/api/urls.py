from django.conf import settings
from django.conf.urls import url

from . import views as todo_view

urlpatterns = [
    url(r'^{}todos'.format(settings.END_POINT_URL), todo_view.TodoListCreateView.as_view(),
        name='get_post_todo'),
    url(r'^{}todo/(?P<pk>[0-9]+)'.format(settings.END_POINT_URL), todo_view.TodoDetailView.as_view(),
        name='get_detail_todo'),
]
