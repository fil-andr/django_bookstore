from django.contrib import admin
from django.urls import path
from .views import books_index, get_authors, by_authors, BookForm, del_book, UpdBook,AuthorForm  # DelBook

urlpatterns = [
    path('', books_index, name='books_index'),
    path('authors/', get_authors, name='authors'),
    path('<int:authors_id>/', by_authors, name='by_authors'),
    path('add_book/', BookForm.as_view(), name='add_book'),
    path('del_book/<int:book_id>/', del_book, name='del_book'),
    path('upd_book/<pk>/', UpdBook.as_view(), name='upd_book'),
    path('add_author/', AuthorForm.as_view(), name='add_author')
]

