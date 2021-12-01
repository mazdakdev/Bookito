from django.urls import path
from . import views

urlpatterns = [
    path("create-category/" , views.create_category , name="create.category"),
    path("read-categories/" , views.get_categories , name="read.category"),
    path("update-category/<int:id>" , views.update_category , name="update.category"),
    path("delete-category/<int:id>" , views.delete_category , name="delete.category"),

    path("create-author/" , views.create_author , name="create.author"),
    path("read-authors/" , views.get_authors , name="read.author"),
    path("update-author/<int:id>" , views.update_author , name="update.author"),
    path("delete-author/<int:id>" , views.delete_author , name="delete.author"),

    path("create-book/" , views.create_book , name="create.book"),
    path("read-books/" , views.read_books , name="read.book"),
    path("get-books-by-category/" , views.get_books_by_category , name="get.category.book"),
    path("get-books-by-author/" , views.get_book_by_author , name="get.author.book"),
    path("get-latest-6-books-decending/" , views.get_latest_updated_books_descending , name="get.latest.decending.book"),
    path("get-latest-6-books-ascending/" , views.get_lastest_updated_books , name="get.latest.ascending.book"),
    path("update-book/<int:id>" , views.update_book , name="update.book"),
    path("delete-book/<int:id>" , views.delete_book , name="delete.book"),


]


