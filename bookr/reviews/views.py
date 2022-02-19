from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Book, Review
from .utils import average_rating


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append(
            {"book": book, "book_rating": book_rating, "number_of_reviews": number_of_reviews}
        )
    context = {"book_list": book_list}
    return render(request, "reviews/books_list.html", context)


def book_details(request, pkid):
    book = get_object_or_404(Book, pk=pkid)
    reviews = book.review_set.all()
    book.avg = average_rating([review.rating for review in reviews])
    return render(request, "reviews/book_details.html", {"book": book, "reviews": reviews})


def fake_db_query_with_many(*args):
    return []


def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", {"name": name})


def index_bad_or(request):
    # Breaks front end with empty string. Just becomes hello
    name = request.GET.get("name", "world")
    # the commented out one is the correct one
    # name = request.GET.get("name") or "world"
    return HttpResponse(f"Hello {name}")


def search(request):
    search = request.GET.get("search") or None
    book_list = fake_db_query_with_many(search)
    return render(request, "book-search.html", {"search": search, "book_list": book_list})


def welcome_view(request):
    return render(request, "base.html")
