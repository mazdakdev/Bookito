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

]


