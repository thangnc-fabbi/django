from rest_framework import serializers
from ... import models


class TodoListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoModel
        fields = (
            'id',
            'content',
            'completed',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
            'is_deleted',
            'version',
        )
        extra_kwargs = {
            'content': {'required': True},
            'completed': {'required': False},
            'created_at': {'read_only': True},
            'created_by': {'read_only': True},
            'updated_at': {'read_only': True},
            'updated_by': {'read_only': True},
            'is_deleted': {'read_only': True},
            'version': {'read_only': True},
        }

    def create(self, validated_data):
        return models.TodoModel.objects.create(content=validated_data['content'])


class ToDoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoModel
        fields = [
            'id',
            'content',
            'completed',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
            'is_deleted',
            'version',
        ]
