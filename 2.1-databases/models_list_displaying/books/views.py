from django.shortcuts import render, redirect
from datetime import datetime

from django.core.paginator import Paginator
from django.urls import reverse

from books.models import Book


def index(request):
    return redirect(reverse('books'))


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
        'pagi': False
    }
    return render(request, template, context)


def books_view_date(request, dt: datetime):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date = dt)
    all_books = Book.objects.order_by('pub_date').all()
    pub_dates = []
    for book in all_books:
        pub_dates.append(book.pub_date.strftime('%Y-%m-%d'))
    pub_dates = list(set(pub_dates))
    pub_dates.sort()
    index_dt = pub_dates.index(dt.strftime('%Y-%m-%d')) + 1

    paginator = Paginator(pub_dates, 1)
    page = paginator.get_page(index_dt)

    prev_page = paginator.get_page(index_dt - 1).object_list[0]
    next_page = paginator.get_page(index_dt + 1).object_list[0]
    context = {
        'books': books,
        'pagi': True,
        'page': page,
        'prev_page': prev_page,
        'next_page': next_page
    }
    return render(request, template, context)