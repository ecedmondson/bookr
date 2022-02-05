from django.http import HttpResponse


def index(request):
    name = request.GET.get("name") or "world"
    return HttpResponse(f"Hello {name}")


def index_bad_or(request):
    # Breaks front end with empty string. Just becomes hello
    name = request.GET.get("name", "world")
    return HttpResponse(f"Hello {name}")
