from django.forms import ModelForm,forms
from .views import Books,Authors
from django.db import models
from .models import Authors

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ('book_title', 'short_desc', 'book_price', 'authors')

class AuthorForm(ModelForm):
    class Meta:
        model = Authors
        fields = ('name',)

# class DelBookForm(ModelForm):
#     class Meta:
#         model = Books
#         fields = ('book_title', 'short_desc', 'book_price', 'authors')