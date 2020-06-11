from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from base import constants
from base.exceptions import ValidationError, CustomValidationError
from todo import models
from .serializers import todo_serializers


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = todo_serializers.TodoListCreateSerializer

    def get_queryset(self):
        return models.TodoModel.objects.filter(is_deleted=False).all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        raise ValidationError(code=constants.ERR_BAD_REQUEST)


class TodoDetailView(APIView):
    def get_object(self, pk):
        try:
            return models.TodoModel.objects.filter(pk=pk, is_deleted=False).get()
        except models.TodoModel.DoesNotExist:
            raise CustomValidationError(code=constants.ERR_RESOURCE_NOT_FOUND)

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializes = todo_serializers.ToDoDetailSerializer(todo)
        return Response(serializes.data)
