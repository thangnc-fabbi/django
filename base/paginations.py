from rest_framework import pagination
from rest_framework.response import Response
import math

from rest_framework.views import APIView


class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

    def get_paginated_response(self, data):
        total_page = math.ceil(self.count / self.limit)
        return Response({
            'links': {
                'prev': self.get_previous_link(),
                'next': self.get_next_link(),
                'count': int(self.count),
                'total_pages': total_page,
            },
            'data': data
        })


class PaginationAPIView(APIView):
    '''
    APIView with pagination
    '''

    pagination_class = CustomPagination

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
