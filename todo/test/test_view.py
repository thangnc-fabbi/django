import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from todo import models
from todo.api.serializers import todo_serializers

client = Client()


class CreateNewTodoTest(TestCase):
    """ Test module for inserting a new todo """

    def setUp(self):
        self.valid_payload = {
            "content": "content",
            "completed": False
        }

        self.invalid_payload = {
            "completed": False
        }

    def test_valid(self):
        response = client.post(
            reverse('get_post_todo'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_corporate_name_required(self):
        response = client.post(
            reverse('get_post_todo'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetAllTodoTest(TestCase):
    def setUp(self):
        models.TodoModel.objects. \
            create(content='test_1')
        models.TodoModel.objects. \
            create(content='test_2')

    def test_get_all_construction_type(self):
        response = client.get(reverse('get_post_todo'))
        # todo = models.TodoModel.objects.filter(is_deleted=False)
        # serializer = todo_serializers.TodoListCreateSerializer(todo, many=True)
        # self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleTodoTTest(TestCase):
    """ Test module for GET single todo API """

    def setUp(self):
        self.test_1 = models.TodoModel.objects.create(content='test 1')
        self.test_2 = models.TodoModel.objects.create(content='test 2')

    def test_get_valid_single_todo(self):
        response = client.get(
            reverse('get_detail_todo', kwargs={'pk': self.test_1.pk}))
        todo = models.TodoModel.objects.get(pk=self.test_1.pk)
        serializer = todo_serializers.ToDoDetailSerializer(todo)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_todo(self):
        response = client.get(
            reverse('get_detail_todo', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
