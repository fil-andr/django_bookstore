from django.shortcuts import render
from django.http import HttpResponse
from .models import Books,Authors
from django.shortcuts import render,redirect
from .forms import BooksForm, AuthorForm      #,DelBookForm
from django.views.generic.edit import CreateView, UpdateView   ##,DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

def books_index(request):
    bks = Books.objects.all()
    auths = Authors.objects.all()
    context = {'bks': bks, 'auths': auths}
    return render(request, 'bookstore/book_index.html', context=context)

def get_authors(request):
    auths = Authors.objects.all()
    context = {'auths': auths}
    return render(request, 'bookstore/get_authors.html', context=context)

def by_authors(request, authors_id):
    bks = Books.objects.filter(authors=authors_id)
    current_author = Authors.objects.get(pk=authors_id)
    authors = Authors.objects.exclude(pk=authors_id)
    context = {'bks': bks, 'current_author': current_author, 'authors': authors}
    return render(request, 'bookstore/books_by_authors.html', context=context)

class BookForm(SuccessMessageMixin,CreateView):
    template_name = 'bookstore/add_book.html'
    form_class = BooksForm
    success_url = reverse_lazy('books_index')
    success_message = 'Книга успешено добавлена, добавленная книга: "%(book_title)s"'

class AuthorForm(SuccessMessageMixin,CreateView):
    template_name = 'bookstore/add_author.html'
    form_class = AuthorForm
    success_url = reverse_lazy('books_index')
    success_message = 'Автор успешено добавлен, добавленный автор: "%(name)s"'


def del_book(request, book_id):
    book = Books.objects.filter(pk=book_id)
    book.delete()
    url_red = reverse_lazy('books_index')
    return redirect(url_red)

class UpdBook(UpdateView):
    template_name = 'bookstore/upd_book.html'
    model = Books
    success_url = reverse_lazy('books_index')
    fields = ['book_title', 'short_desc', 'book_price']