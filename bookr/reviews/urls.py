from django.urls import path
from . import views


urlpatterns = [
    path("", views.welcome_view, name="welcome"),
    path("books/", views.book_list, name="book_list"),
    path("book/<int:pkid>/", views.book_details, name="book_details"),
]
