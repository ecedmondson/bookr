from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "publication_date"
    list_display = ("title", "isbn")
    list_filter = ("publisher", "publication_date")
    search_fields = ("title", "isbn")
    fields = ("content", "rating", "creator", "book")


class ContributorAdmin(admin.ModelAdmin):
    _name_attrs = ("last_names", "first_names")
    list_display = _name_attrs
    search_fields = _name_attrs
    list_filter = ("last_names",)


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
