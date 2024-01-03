from django.urls import path

from books.views import BookList


urlpatterns = [
    path("book_list/", BookList)
]