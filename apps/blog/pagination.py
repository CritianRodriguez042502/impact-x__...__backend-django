from rest_framework.pagination import PageNumberPagination

class SmallPagination (PageNumberPagination):
    page_query_param = "page"
    page_size = 3
    max_page_size = 3


class MediumPagination (PageNumberPagination):
    page_query_param = "page"
    page_size = 5
    max_page_size = 5
    

class BigPagination (PageNumberPagination):
    page_query_param = "page"
    page_size = 8
    max_page_size = 8


class PaginationCommentsBlog (PageNumberPagination) :
    page_query_param = "page"
    page_size = 11
    max_page_size = 11