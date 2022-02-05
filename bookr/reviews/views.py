from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", {"name": name})


def index_bad_or(request):
    # Breaks front end with empty string. Just becomes hello
    name = request.GET.get("name", "world")
    # the commented out one is the correct one
    # name = request.GET.get("name") or "world"
    return HttpResponse(f"Hello {name}")
