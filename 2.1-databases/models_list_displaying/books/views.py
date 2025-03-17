from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def book_view(request, pub_date):
    books_list = Paginator(Book.objects.all(), 1)
    pub_dates = Book.objects.values_list('pub_date', flat=True).distinct()
    pagi = request.GET.get(pub_date)
    page = pagi.get_page(pagi)
    template = 'books/book.html'
    books = Book.objects.filter(pub_date=pub_date)
    context = {
        'page': page,
        'books': books
    }
    return render(request, template, context)