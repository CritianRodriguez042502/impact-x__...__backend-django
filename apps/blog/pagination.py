from rest_framework.pagination import PageNumberPagination

class SmallPagination (PageNumberPagination):
    page_query_param = "page"
    page_size = 3
    max_page_size = 3


class MediumPagination (PageNumberPagination):
    page_query_param = "page"
    page_size = 6
    max_page_size = 6
    

class BigPagination (PageNumberPagination):
    page_query_param = "page"
    page_size = 8
    max_page_size = 8