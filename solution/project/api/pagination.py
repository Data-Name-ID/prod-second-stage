import rest_framework.pagination
import rest_framework.response


class Pagination(rest_framework.pagination.LimitOffsetPagination):
    default_limit = 5

    def get_paginated_response(self, data):
        return rest_framework.response.Response(data)
