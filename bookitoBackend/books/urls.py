from django.urls import path
from . import views

urlpatterns = [

    path("create-book/" , views.create_book , name="create.book"),
    path("read-books/" , views.read_books , name="read.book"),
    path("update-book/<int:id>" , views.update_book , name="update.book"),
    path("delete-book/<int:id>" , views.delete_book , name="delete.book"),

    path("get-book/<int:id>" , views.get_book_by_id , name="get.id.book"),

    path("get-books-by-category/" , views.get_books_by_category , name="get.category.book"),
    path("get-books-by-author/" , views.get_book_by_author , name="get.author.book"),
    path("get-latest-6-books-decending/" , views.get_latest_updated_books_descending , name="get.latest.decending.book"),
    path("get-latest-6-books-ascending/" , views.get_lastest_updated_books , name="get.latest.ascending.book"),

    path("books/" , views.Search_books , name="search.book"),


]


