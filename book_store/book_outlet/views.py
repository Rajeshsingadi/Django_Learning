from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg

# Create your views here.
from .models import Book


def index(request):
    books = Book.objects.all().order_by("title")

    # books = Book.objects.all().order_by("-title")#descending order
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "Number_of_the_Books": num_books,
        "Average_Rating": avg_rating
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })
