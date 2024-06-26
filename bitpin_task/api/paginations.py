from rest_framework import pagination


class ProductPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 10000


class ProductRatingPagination(pagination.PageNumberPagination):
    page_size = 50
    page_query_param = "page_size"
    max_page_size = 10000