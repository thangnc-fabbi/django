from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name='Created At')
    created_by = models.IntegerField(null=True, blank=True, verbose_name='Created By')
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True, verbose_name='Updated At')
    updated_by = models.IntegerField(null=True, blank=True, verbose_name='Updated By')
    is_deleted = models.BooleanField(null=True, default=False, verbose_name='IsDeleted')
    version = models.IntegerField(null=True, blank=True, verbose_name='Version', default=1)

    class Meta:
        abstract = True
