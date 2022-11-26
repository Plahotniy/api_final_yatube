from rest_framework.pagination import BasePagination
from rest_framework.response import Response

class PostPagination(BasePagination):
    def get_paginated_response(self, data):
        return Response({"results": data})
