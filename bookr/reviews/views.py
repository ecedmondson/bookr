from django.http import HttpResponse
from django.shortcuts import render

from .models import Book


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
    message = f"""
       <html>
           <h1>Welcome to Bookr!</h1>
            <p>{Book.objects.count()} books and counting!</p>
        </html>"
    """
    return HttpResponse(message)
