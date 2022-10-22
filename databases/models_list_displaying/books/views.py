from django.shortcuts import render
from .models import Book
import datetime

def books_view(request):
    template = 'books/books_list.html'

    context = {
        'books': Book.objects.all()
    }
    return render(request, template, context)


def books_by_date_view(request,date):
    template = 'books/books_list.html'
    requested_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    end_of_day = requested_date + datetime.timedelta(hours=24, minutes=59, seconds=59)
    books = Book.objects.filter(pub_date__gte=requested_date,
                                    pub_date__lte=end_of_day)
    left = Book.objects.filter(pub_date__lt=requested_date).order_by("-pub_date")
    right = Book.objects.filter(pub_date__gte=end_of_day).order_by("pub_date")

    context = {
        'books': books,
        'page_back': left[0] if len(left) > 0 else None,
        'page_forward': right[0] if len(right) > 0 else None
    }
    return render(request, template, context)

