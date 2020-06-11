from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator, qs_exists

from base import constants


class CustomUniqueTogetherValidator(UniqueTogetherValidator):
    def __init__(self, queryset, fields):
        self.queryset = queryset
        self.fields = fields
        self.serializer_field = None
        self.message = self.message

    def __call__(self, attrs, serializer):
        self.enforce_required_fields(attrs, serializer)
        queryset = self.queryset
        queryset = self.filter_queryset(attrs, queryset, serializer)
        queryset = self.exclude_current_instance(attrs, queryset, serializer.instance)

        # Ignore validation if any field is None
        checked_values = [
            value for field, value in attrs.items() if field in self.fields
        ]
        if None not in checked_values and qs_exists(queryset):
            field_names = ', '.join(self.fields)
            message = self.message.format(field_names=field_names)
            field = ''.join(self.fields[0].split('_'))
            raise ValidationError({field: message}, code=constants.ERR_UNIQUE_FIELD)
