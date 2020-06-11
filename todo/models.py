from django.db import models
from base.models import BaseModel


class TodoModel(BaseModel):
    id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ToDo ID')
    content = models.CharField(null=False, max_length=100, blank=False, verbose_name='Content')
    completed = models.BooleanField(null=True, blank=True, default=False, verbose_name='Completed')

    class Meta:
        db_table = 'tb_todo'
        verbose_name = 'todo'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['is_deleted']),
        ]
        ordering = ['-id']
